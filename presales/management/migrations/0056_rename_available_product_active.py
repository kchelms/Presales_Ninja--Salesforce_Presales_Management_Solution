# Generated by Django 3.2.12 on 2022-04-13 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0055_alter_note_note_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='active',
        ),
    ]
