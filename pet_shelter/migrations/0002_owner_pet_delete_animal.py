# Generated by Django 4.0.4 on 2022-06-04 09:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shelter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_of_pet', models.CharField(choices=[('CT', 'cat'), ('DG', 'dog'), ('PT', 'parrot')], default='CT', max_length=2)),
                ('pet_name', models.CharField(max_length=100)),
                ('pet_age', models.PositiveSmallIntegerField()),
                ('pet_breed', models.CharField(max_length=100)),
                ('pet_color', models.CharField(max_length=30)),
                ('treated_for_parasites', models.BooleanField(default=False)),
                ('vaccinated', models.BooleanField(default=False)),
                ('receipt_date', models.DateField(default=datetime.date.today)),
                ('new_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_owner', to='pet_shelter.owner')),
                ('previous_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prev_owner', to='pet_shelter.owner')),
            ],
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
    ]
