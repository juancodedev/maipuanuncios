from django.shortcuts import render
from django.views.generic import ListView
from apps.home.models import advertisement

# Create your views here.

class HomeList(ListView):
    model = advertisement
    template_name = 'home.html'