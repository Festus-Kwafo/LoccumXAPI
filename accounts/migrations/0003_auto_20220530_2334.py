# Generated by Django 3.1.2 on 2022-05-30 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220523_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='id_file',
        ),
        migrations.RemoveField(
            model_name='locum',
            name='id_file',
        ),
        migrations.RemoveField(
            model_name='locum',
            name='license_file',
        ),
    ]
