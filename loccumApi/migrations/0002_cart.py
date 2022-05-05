# Generated by Django 3.1.2 on 2022-05-05 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220430_1151'),
        ('loccumApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ManyToManyField(to='loccumApi.Job')),
            ],
            options={
                'ordering': ['cart_id', '-created_at'],
            },
        ),
    ]
