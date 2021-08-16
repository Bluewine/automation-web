import json
import os
import shutil

import requests

from core.settings import BASE_DIR
from libs.amt_helpers import generate_build_file, generate_package
from libs.interactor.interactor import Interactor
from main.interactors.list_dataflow_interactor import DataflowListInteractor


class DownloadDataflowInteractor(Interactor):
    def run(self):
        _exc = None
        try:
            # Deletes first the retrieve folder.
            if os.path.isdir(f"{BASE_DIR}/ant/{self.context.user.username}/retrieve"):
                shutil.rmtree(f"{BASE_DIR}/ant/{self.context.user.username}/retrieve")

            generate_build_file(self.context.model, self.context.user)

            members = [f"<members>{dataflow_name}</members>" for dataflow_name in self.context.dataflow]
            generate_package(members, self.context.user)

            cur_dir_tmp = "_CUR_DIR_TMP_"
            _cmd_queue = [
                F"export {cur_dir_tmp}=$(pwd)",
                f"cd {BASE_DIR}/ant/{self.context.user.username}",

                f"{BASE_DIR}/libs/apache_ant/bin/ant downloadDataflows",

                f"cd ${cur_dir_tmp}",
                f"unset {cur_dir_tmp}"
            ]
            os.system(" && ".join(_cmd_queue))
        except Exception as e:
            _exc = e

        self.context.exception = _exc


class DownloadDataflowInteractorNoAnt(Interactor):
    def run(self):
        _exc = None
        user = self.context.user
        model = self.context.model
        dataflows = self.context.dataflow

        downloaded_dataflows_defs = {}

        try:
            if not model.instance_url:
                raise ConnectionError(f"The instance <code>{model.name}</code> is not loged in. Please login first.")

            down_all_ctx = DataflowListInteractor.call(model=model, search=None,
                                                       refresh_cache='true',
                                                       user=user)
            if down_all_ctx.error:
                raise Exception(down_all_ctx.error)

            # Deletes first the retrieve folder.
            if os.path.isdir(f"{BASE_DIR}/ant/{self.context.user.username}/retrieve"):
                shutil.rmtree(f"{BASE_DIR}/ant/{self.context.user.username}/retrieve")

            output_path = f"{BASE_DIR}/ant/{self.context.user.username}/retrieve/dataflow/wave/"
            os.makedirs(output_path)

            for dataflow in dataflows:
                resource = '/services/data/v51.0/wave/dataflows/'
                url = model.instance_url + resource + down_all_ctx.df_ids_api[dataflow]
                url = url.strip()
                header = {'Authorization': "Bearer " + model.oauth_access_token, 'Content-Type': 'application/json'}

                response = requests.get(url, headers=header)

                if response.status_code == 200:
                    response = response.json()
                    definition = response['definition']
                    filename = f"{dataflow}.wdf"
                    filepath = output_path + filename
                    print(filepath)
                    with open(filepath, 'w') as f:
                        json.dump(definition, f, indent=2)
                else:
                    raise ConnectionError(output_path)

        except Exception as e:
            _exc = e
            downloaded_dataflows_defs = {}
        finally:
            self.context.exception = _exc
            self.context.downloaded_df_defs = downloaded_dataflows_defs
