from django.db import models
from apps.home.models import advertisement
from apps.admins.models import user
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Ratings(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    UserRating = models.ForeignKey(user, on_delete=models.CASCADE, default=None)
    rating_stars = models.IntegerField('Evaluacion de Locales',null=True,blank=True,validators=[MinValueValidator(1), MaxValueValidator(5)], choices=RATING)
    advertisementRating = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)
    #advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
         return str(self.UserRating)
