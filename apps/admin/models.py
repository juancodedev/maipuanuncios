from django.db import models
import uuid
from apps.home.models import advertisement

# Create your models here.
class  roles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)

class user(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField
    password = models.CharField
    role = models.ForeignKey(roles, on_delete=models.CASCADE, default=None) 
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rut = models.CharField(max_length=14)
    advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None) 



