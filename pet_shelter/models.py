from django.db import models
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Owner(models.Model):
    full_name = models.CharField(max_length=120)
    phone = PhoneNumberField(unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.full_name}"


class Breed(models.Model):
    breed_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.breed_name}"


class Color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.color_name}"


class Pet(models.Model):
    PETS_KINDS = [
        ('CT', 'cat'),
        ('DG', 'dog'),
        ('PT', 'parrot')
    ]
    kind_of_pet = models.CharField(max_length=2,
                                   choices=PETS_KINDS,
                                   default='CT',
                                   verbose_name='Вид животного')
    pet_name = models.CharField(max_length=100, verbose_name='Кличка')
    pet_photo = models.ImageField(upload_to='photos', blank=True)
    pet_age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    pet_breed = models.ForeignKey(Breed, on_delete=models.CASCADE,
                                  related_name="breed",
                                  null=True, blank=True)
    pet_color = models.ForeignKey(Color, on_delete=models.CASCADE,
                                  related_name="color",
                                  null=True, blank=True)
    description = models.TextField(null=True)
    treated_for_parasites = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)
    receipt_date = models.DateField(default=date.today)
    previous_owner = models.ForeignKey(Owner, on_delete=models.CASCADE,
                                       related_name="prev_owner",
                                       null=True, blank=True)
    new_owner = models.ForeignKey(Owner, on_delete=models.CASCADE,
                                  related_name="new_owner",
                                  null=True, blank=True)

    def __str__(self):
        return f"{self.pet_name}"
