# Generated by Django 3.1.6 on 2021-02-13 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HelpDepu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association',
            name='NumEnt',
        ),
    ]
