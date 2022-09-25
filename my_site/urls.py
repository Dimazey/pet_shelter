"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from pet_shelter import views
from django.conf import settings
from pet_shelter.views import PetDetailView

urlpatterns = [
    path('', views.PetListView.as_view()),
    path('admin/', admin.site.urls),
    path('index/', views.PetListView.as_view()),
    path('<int:pk>/', PetDetailView.as_view()),
    path('about/', views.about),
    path('contact/', views.contact),
    path('list/<category>/', views.PetListView.as_view()),
    path('gettohome/<int:pk>/', views.GetToHomeFormView.as_view()),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
