from django.shortcuts import render
from django.views.generic import ListView
from apps.home.models import advertisement
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
        times_p = [
            "00:00",
            "00:30",
            "01:00",
            "01:30",
            "02:00",
            "02:30",
            "03:00",
            "03:30",
            "04:00",
            "04:30",
            "05:00",
            "05:30",
            "06:00",
            "06:30",
            "07:00",
            "07:30",
            "08:00",
            "08:30",
            "09:00",
            "09:30",
            "10:00",
            "10:30",
            "11:00",
            "11:30",
            "12:00",
            "12:30",
            "13:00",
            "13:30",
            "14:00",
            "14:30",
            "15:00",
            "15:30",
            "16:00",
            "16:30",
            "17:00",
            "17:30",
            "18:00",
            "18:30",
            "19:00",
            "19:30",
            "20:00",
            "20:30",
            "21:00",
            "21:30",
            "22:00",
            "22:30",
            "23:00",
            "23:30"
                ]
        for adv in advertisements:
            rating = 5 # Ratings.objects.filter(Schools=escuela.Id).aggregate(Avg('Score'))['Score__avg']
            # if now.hour >= adv.open_from and now.hour <= adv.open_to:
            #     op =  True
            # else:
            #     op = False
            # count = 1
            # for x in times_p:
            #     if x.split(':')[0] == str(now.hour) and x.split(':')[1] == "00":
            #         break
            #     count=+count+1
            #     strptime(string[, format])
            #     strptime(date_string, %H)


            # if now.minute >= adv.open_from and now.minute <= adv.open_to:
            #     op =  True
            # else:
            #     op = False
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

