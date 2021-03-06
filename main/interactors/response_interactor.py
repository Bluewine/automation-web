import json
import os
import shutil
import zipfile

from django.conf import settings
from django.http import HttpResponse

from libs.interactor.interactor import Interactor
from main.interactors.dataflow_tree_manager import show_in_browser
from main.models import DataflowUploadHistory


# Source: https://pybit.es/articles/django-zipfiles/
class FileResponseInteractor(Interactor):
    def run(self):

        try:
            response = HttpResponse(content_type='application/zip')
            zf = zipfile.ZipFile(response, 'w')
            mypath = self.context.zipfile_path
            onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
            for file in onlyfiles:
                with open(f"{mypath}{file}") as f:
                    json_str = json.dumps(json.load(f), indent=2)
                    zf.writestr(file, json_str)
            response['Content-Disposition'] = f'attachment; filename={self.context.zipfile_name} dataflows.zip'
            self.context.response = response
        except Exception as e:
            self.context.exception = e


class ZipFileResponseInteractor(Interactor):
    def run(self):

        try:
            zipfile = open(self.context.zipfile_path, 'rb')
            response = HttpResponse(zipfile, content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename={self.context.envname} dataflows.zip'
            self.context.response = response
        except Exception as e:
            self.context.exception = e


class JsonFileResponseInteractor(Interactor):
    def run(self):
        try:
            filepath = self.context.filepath
            filename = os.path.basename(filepath)
            file = open(filepath, 'rb')
            response = HttpResponse(file,
                                    content_type='application/json',
                                    headers={
                                        'Content-Disposition': f"attachment; filename={filename}"
                                                               f"{'.json' if filename[-5:] != '.json' else ''}"
                                    })
            self.context.response = response
        except Exception as e:
            self.context.exception = e


class UploadedDataflowToZipResponse(Interactor):
    def run(self):
        model: DataflowUploadHistory = self.context.model
        user = self.context.user

        original_df = json.dumps(model.original_dataflow, indent=2)
        uploaded_df = json.dumps(model.uploaded_dataflow, indent=2)

        path = settings.MEDIA_ROOT + f"/uploaded-dataflow-to-zip/"
        usr_path = path + user.username

        original_path = usr_path + '/original.json'
        uploaded_path = usr_path + '/uploaded.json'

        if not os.path.isdir(usr_path):
            os.makedirs(usr_path)

        json.dump(model.original_dataflow, open(original_path, 'w+'), indent=2)
        json.dump(model.uploaded_dataflow, open(uploaded_path, 'w+'), indent=2)

        show_in_browser(original_path, uploaded_path)
        html_filepath = f'{settings.BASE_DIR}/main/templates/json_diff_output.html'
        while not os.path.isfile(html_filepath):
            pass

        with open(html_filepath, 'r') as f:
            html = f.read().encode('utf-8')
        os.remove(html_filepath)
        shutil.rmtree(path)

        response = HttpResponse(content_type='application/zip')
        zf = zipfile.ZipFile(response, 'w')
        zf.writestr(f"{model.dataflow_name}.json", original_df)
        zf.writestr(f"{model.dataflow_name}--uploaded.json", uploaded_df)
        zf.writestr(f"difference visualizer.html", html)

        response['Content-Disposition'] = f'attachment; filename={model.dataflow_name}.zip'
        self.context.response = response
