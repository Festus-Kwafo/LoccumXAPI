# Generated by Django 3.1.2 on 2022-05-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loccumApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='name_organization',
            field=models.CharField(max_length=255, null=True),
        ),
    ]