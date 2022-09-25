from django.template import loader
from django.http import HttpResponse
from pet_shelter.models import Pet
from django.views.generic import DetailView, ListView, FormView
from pet_shelter.Forms import GetToHomeForm
from django.shortcuts import get_object_or_404


# Create your views here.

class PetDetailView(DetailView):
    model = Pet


def about(request):
    template = loader.get_template('about.html')
    pet_count = Pet.objects.count()
    about_data = {
        'title': 'О приюте',
        'pet_count': pet_count,
    }
    return HttpResponse(template.render(about_data))


def contact(request):
    template = loader.get_template('contact.html')
    contact_data = {
        'title': 'Наши контакты',
    }
    return HttpResponse(template.render(contact_data))


class PetListView(ListView):

    def __init__(self, category='CT'):
        self.category = category

    model = Pet
    template_name = "pet_list.html"

    def get_queryset(self, **kwargs):
        category = self.kwargs.get('category', None)
        qs = super().get_queryset(**kwargs)
        if category is not None:
            self.category = category
            return qs.filter(kind_of_pet=category)
        else:
            return qs.filter(kind_of_pet='CT')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = {
            'CT': '1',
            'DG': '2',
            'PT': '3'
        }
        context['recent_link'] = categories[self.category]
        context['title'] = 'Наши питомцы'
        return context


class GetToHomeFormView(FormView):
    template_name = 'gettohome.html'
    form_class = GetToHomeForm
    success_url = '/thanks/'

    def get_initial(self):
        obj = get_object_or_404(Pet, pk=self.kwargs['pk'])
        initial = super().get_initial()
        initial['pk'] = obj.pk
        initial['pet_name'] = obj.pet_name

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_name"] = get_object_or_404(Pet, pk=self.kwargs['pk']).pet_name

        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
