# Generated by Django 4.0.4 on 2022-05-27 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_of', models.CharField(choices=[('ct', 'Кошка'), ('dg', 'Собака'), ('pa', 'Попугай')], default='ct', max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('breed', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
                ('treated_for_parasites', models.BooleanField(default=False)),
                ('vaccinated', models.BooleanField(default=False)),
                ('receipt_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]