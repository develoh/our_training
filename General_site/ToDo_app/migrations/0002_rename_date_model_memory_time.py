# Generated by Django 4.2.3 on 2023-07-29 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_memory',
            old_name='date',
            new_name='time',
        ),
    ]
