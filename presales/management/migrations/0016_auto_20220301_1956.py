# Generated by Django 3.2.12 on 2022-03-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20220224_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='oneDateTime',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='selectedDateTime',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='threeDateTime',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='twoDateTime',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
