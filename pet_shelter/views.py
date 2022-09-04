from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from pet_shelter.models import Pet, Owner, Breed, Color
from django.views.generic import DetailView, ListView


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    pets = Pet.objects.all().filter(kind_of_pet='CT')
    pets_data ={
        'title': 'наши питомцы',
        'pets': pets,
        'recent_link': '1',
    }

    return HttpResponse(template.render(pets_data))

def dog(request):
    template = loader.get_template('index.html')
    pets = Pet.objects.all().filter(kind_of_pet='DG')
    pets_data ={
        'title': 'наши питомцы',
        'pets': pets,
        'recent_link': '2',
    }

    return HttpResponse(template.render(pets_data))

def parrot(request):
    template = loader.get_template('index.html')
    pets = Pet.objects.all().filter(kind_of_pet='PT')
    pets_data = {
        'title': 'наши питомцы',
        'pets': pets,
        'recent_link': '3',
    }

    return HttpResponse(template.render(pets_data))

class PetDetailView(DetailView):
    model = Pet

def about(request):
    template = loader.get_template('about.html')
    pet_count = Pet.objects.count()
    about_data = {
        'pet_count': pet_count,
    }
    return HttpResponse(template.render(about_data))

class PetListView(ListView):
    model = Pet
    template_name = "pet_list.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(kind_of_pet='CT')






