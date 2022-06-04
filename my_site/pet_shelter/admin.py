from django.contrib import admin
from pet_shelter.models import Pet, Owner, Breed, Color
# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

