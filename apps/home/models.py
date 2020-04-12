from django.db import models
import uuid

# Create your models here.
class advertisement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Type = models.CharField
    Social_network = models.CharField
    phones = models.CharField
    email = models.CharField                
    url_website = models.CharField
    address = models.CharField
    description  = models.CharField         
    image = models.ImageField
    logo  = models.ImageField
    latitude_longitude = models.CharField
    incorporation_date = models.DateField
    subscription_type = models.CharField
    state = models.BooleanField
    includes_maps  = models.CharField
    credits_id     = models.CharField

class credits_history(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_recharge = models.TimeField
    amount = models.IntegerField()
    time_recharge = models.TimeField(auto_now=False, auto_now_add=False)

class credits(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    current_amount = models.IntegerField()
    days = models.IntegerField()

class social_networks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    user_socialNetwork = models.CharField(max_length=50)
    advertisement_id =  models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)

class subscription_plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50)
    amount = models.IntegerField
    valid_from = models.DateField(auto_now=True, auto_now_add=False)
    valid_to = models.DateField(auto_now=False, auto_now_add=False)

class phones(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)
    Number = models.CharField(max_length=12)
    wsp = models.BooleanField
    advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)

class type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50)
    advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)