# Generated by Django 5.0.4 on 2024-04-27 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_description_task_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='folio',
            new_name='identificador',
        ),
    ]
