# Generated by Django 3.0.14 on 2021-12-01 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20211201_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(help_text='Year-Month-Day'),
        ),
        migrations.AlterField(
            model_name='date',
            name='time',
            field=models.TimeField(),
        ),
    ]
