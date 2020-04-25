from django.db import models
#from phonenumber_field import PhoneNumberField
#from apps.evaluate.models import Ratings

import uuid

# Create your models here.

class NameSocialNetworks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NameDescriptions = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.NameDescriptions

class social_networks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_socialNetwork = models.CharField(max_length=50)
    red = models.ManyToManyField(NameSocialNetworks, default=None)
    
    def __str__(self):
        return self.user_socialNetwork

class credits(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_recharge = models.TimeField
    amount = models.IntegerField()
    time_recharge = models.TimeField(auto_now=False, auto_now_add=False, default=None)
    #advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.amount)

class phones(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typePhone = models.CharField(max_length=50)
    Number = models.CharField(max_length=12)
    wsp = models.BooleanField
    #advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.Number


class typeA(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50)
    #advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.description

class subscription_plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50)
    amount = models.IntegerField
    valid_from = models.DateField(auto_now=True, auto_now_add=False)
    valid_to = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.description

class advertisement(models.Model):
    HOURS = (
    (1, '00:00'),
    (2, '00:30'),
    (3, '01:00'),
    (4, '01:30'),
    (5, '02:00'),
    (6, '02:30'),
    (7, '03:00'),
    (8, '03:30'),
    (9, '04:00'),
    (10, '04:30'),
    (11, '05:00'),
    (12, '05:30'),
    (13, '06:00'),
    (14, '06:30'),
    (15, '07:00'),
    (16, '07:30'),
    (17, '08:00'),
    (18, '08:30'),
    (19, '09:00'),
    (20, '09:30'),
    (21, '10:00'),
    (22, '10:30'),
    (23, '11:00'),
    (24, '11:30'),
    (25, '12:00'),
    (26, '12:30'),
    (27, '13:00'),
    (28, '13:30'),
    (29, '14:00'),
    (30, '14:30'),
    (31, '15:00'),
    (32, '15:30'),
    (31, '16:00'),
    (32, '16:30'),
    (19, '17:00'),
    (20, '17:30'),
    (21, '18:00'),
    (22, '18:30'),
    (23, '19:00'),
    (24, '19:30'),
    (25, '20:00'),
    (26, '20:30'),
    (27, '21:00'),
    (28, '21:30'),
    (29, '22:00'),
    (30, '22:30'),
    (31, '23:00'),
    (32, '23:30')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default = None, max_length=50)
    Type_advertisement = models.ForeignKey(typeA, on_delete=models.CASCADE, default=None)
    Social_network = models.ManyToManyField(social_networks, default=None)
    phones = models.ManyToManyField(phones, default=None)
    #PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254, default=None)                
    url_website = models.URLField(max_length=200, default=None)
    address = models.CharField
    description  = models.CharField         
    image = models.ImageField
    logo  = models.ImageField
    latitude_longitude = models.CharField
    incorporation_date = models.DateField
    subscription_type = models.ForeignKey(subscription_plan, on_delete=models.CASCADE, default=None)
    state = models.BooleanField
    includes_maps  = models.CharField
    credits_id     = models.ForeignKey(credits, on_delete=models.CASCADE, default=None)
    open_from = models.IntegerField(choices=HOURS, default=None)
    open_to = models.IntegerField(choices=HOURS, default=None)
    #rating = models.ForeignKey(Ratings, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    def get_socialNetwork(self):
        return self.Social_network.name
        # return ', '.join([s.name for s in self.Social_network_set.all()])
    
    get_socialNetwork.shot_description = 'Redes Sociales'
