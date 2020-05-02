from django.shortcuts import render
from django.views.generic import ListView
from apps.home.models import advertisement, OpeningHours, SpecialDays
from apps.evaluate.models import Ratings
from datetime import datetime
from django.db.models import Avg

# Create your views here.

class HomeList(ListView):
    model = advertisement
    template_name = 'home.html'
    #paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(HomeList,self).get_context_data(**kwargs)
        advertisements = advertisement.objects.all().order_by('name')
        now = datetime.now()
        data = []
        for adv in advertisements:
            OpH = 0
            rating = Ratings.objects.filter(advertisementRating=adv.id).aggregate(Avg('rating_stars'))['rating_stars__avg']
            countRatings = Ratings.objects.filter(advertisementRating=adv.id).count()
            OpH = OpeningHours.objects.filter(store = adv.id, weekday_from = now.strftime("%w"))[1]
            #HourFrom =OpeningHours.objects.filter(store = adv.id, weekday_from = now.strftime("%w"))[0].from_hour
            # HourTo = OpeningHours.objects.filter(store = adv.id, weekday_from = now.strftime("%w")).value('to_hour')
            #OpeningHours.from_hour
            # print(OpH.from_hour)
            # print(OpH.to_hour)
            # print(now.strftime("%H"))
            # if int(OpH.from_hour) <= int(now.strftime("%H")) and int(OpH.to_hour) >= int(now.strftime("%H")):
            #     op = True
            # else:
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
            'countRatings': countRatings
        }
            data.append(dic)

        context['data'] = data
        return context

