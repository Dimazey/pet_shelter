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

    def __init__(self, category='CT'):
        self.category = category

    model = Pet
    template_name = "pet_list.html"

    def get_queryset(self, **kwargs):
        category = self.kwargs.get('category', None)
        qs = super().get_queryset(**kwargs)
        if category is not None:  # если аргумент существует
            self.category = category
            return qs.filter(kind_of_pet=category)
        else:
            return qs.filter(kind_of_pet='CT')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.category)
        categories = {
            'CT': '1',
            'DG': '2',
            'PT': '3'
        }

        context['recent_link'] = categories[self.category]

        return context





