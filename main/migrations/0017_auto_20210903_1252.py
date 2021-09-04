# Generated by Django 3.2.3 on 2021-09-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210903_1143'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='profile',
            name='unique key per user',
        ),
        migrations.AddConstraint(
            model_name='profile',
            constraint=models.UniqueConstraint(fields=('key', 'user_id'), name='Unique Key constraint per User is enforced'),
        ),
    ]