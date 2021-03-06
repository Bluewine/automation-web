# Generated by Django 3.2.3 on 2021-09-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210903_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='key',
            field=models.CharField(max_length=128),
        ),
        migrations.AddConstraint(
            model_name='profile',
            constraint=models.UniqueConstraint(fields=('key', 'user_id'), name='unique key per user'),
        ),
    ]
