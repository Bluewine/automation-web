# Generated by Django 3.2.3 on 2021-07-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='user_specific_folder',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]