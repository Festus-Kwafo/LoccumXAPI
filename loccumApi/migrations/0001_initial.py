# Generated by Django 3.1.2 on 2022-04-30 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20220430_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('title', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('salary', models.FloatField()),
                ('job_type', models.CharField(choices=[('PERMANENT', 'Permanent'), ('SHIFT', 'Shift')], max_length=20, null=True)),
            ],
        ),
    ]
