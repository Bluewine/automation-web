# Generated by Django 3.2.3 on 2021-07-28 19:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import main.modelfields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_notifications_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataflowDeprecation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=1024)),
                ('original_dataflow', main.modelfields.CompressedJSONField()),
                ('deprecated_dataflow', main.modelfields.CompressedJSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]