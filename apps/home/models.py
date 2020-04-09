from django.db import models
import uuid

# Create your models here.
class credits(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    current_amount = models.IntegerField()
    days = models.IntegerField()

class advertisement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)