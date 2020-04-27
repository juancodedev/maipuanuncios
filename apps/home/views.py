from django.shortcuts import render
from django.views.generic import ListView
from apps.home.models import advertisement, OpeningHours, SpecialDays
from datetime import datetime

# Create your views here.

class HomeList(ListView):
    model = advertisement
    template_name = 'home.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(HomeList,self).get_context_data(**kwargs)
        advertisements = advertisement.objects.all().order_by('name')
        now = datetime.now()
        data = []
        for adv in advertisements:
            rating = 5 # Ratings.objects.filter(Schools=escuela.Id).aggregate(Avg('Score'))['Score__avg']
            
            op = False
            dic = {
            'id' : adv.id,
            'name': adv.name,
            'Type_advertisement': adv.Type_advertisement,
            'Score': rating, 
            'description' : adv.description,
            'image': adv.image,
            'logo' : adv.logo,
            'latitude_longitude': adv.latitude_longitude,
            'state': adv.state,
            'open': op,
            'price_from' : adv.price_from, 
            'price_to' : adv.price_to,
        }
            data.append(dic)

        context['data'] = data
        return context

