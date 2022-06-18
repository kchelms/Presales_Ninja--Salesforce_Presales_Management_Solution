# Generated by Django 3.0.14 on 2021-12-01 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('date_ID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('opportunityName', models.CharField(max_length=100)),
                ('opportunity_ID', models.IntegerField(default=0)),
                ('account_ID', models.IntegerField(default=0)),
                ('salesmemeber', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('oneDates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oneDates', to='management.Dates')),
                ('threeDates', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threeDates', to='management.Dates')),
                ('twoDates', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='twoDates', to='management.Dates')),
            ],
        ),
    ]