# Generated by Django 3.2.7 on 2021-10-21 20:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import main.modelfields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0025_alter_specialpermissions_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataflowUploadHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_dataflow', main.modelfields.CompressedJSONField()),
                ('uploaded_dataflow', main.modelfields.CompressedJSONField()),
                ('dataflow_name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('salesforce_env',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                   to='main.salesforceenvironment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
