# Generated by Django 5.0.4 on 2024-04-27 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_folio_cliente_identificador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='identificador',
        ),
    ]
