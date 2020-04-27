from django.shortcuts import render
from django.views.generic import ListView
from apps.home.models import advertisement

# Create your views here.
class Admins(ListView):
    model = advertisement
    template_name = 'admins.html'
    paginate_by = 6

class Forms(ListView):
    model = advertisement
    template_name = 'forms_add.html'

class AllList(ListView):
    model = advertisement
    template_name = 'admin_all.html'

