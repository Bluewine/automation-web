# Generated by Django 3.2.3 on 2021-08-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_dataflowdeprecation_deprecationdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='message',
            field=models.CharField(max_length=4096),
        ),
    ]
