from django.shortcuts import render
from django.views.generic import ListView
from apps.home.models import advertisement

# Create your views here.
class Admins(ListView):
    model = advertisement
    template_name = 'admins.html'

