# Generated by Django 3.1.2 on 2022-05-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loccumApi', '0002_job_name_organization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='salary',
            new_name='max_salary',
        ),
        migrations.AddField(
            model_name='job',
            name='min_salary',
            field=models.FloatField(default=789),
            preserve_default=False,
        ),
    ]