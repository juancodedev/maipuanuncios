from django.db import models
import uuid

# Create your models here.
class credits(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    current_amount = models.IntegerField()
    days = models.IntegerField()

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
    id1            = models.CharField 
    user_id        = models.CharField 
    credits_id     = models.CharField

# class Ratings(models.Model):
#         RATING = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#     )

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     #Score = models.IntegerField(choices=RATING)
#     Score = models.IntegerField('Evaluacion de la escuela',null=True,blank=True,validators=[MinValueValidator(1), MaxValueValidator(5)])
#     Schools = models.ForeignKey(School, on_delete=models.CASCADE, default=None)
#     #comment = models.TextField('Comentario asociado a la escuela',max_length=500,blank=True)

#     def __str__(self):
#          return str(self.User)
#         #return

#     def display_School(self):
#         return self.Schools.Name
#         #', '.join([ Schools.Name for Schools in self.Schools.all()[:3] ])
#     display_School.short_description = 'Escuela'

#     def get_user(self):
#         return self.User.Name+' '+self.User.Last_Name
#         #', '.join([ User.Name for User in self.User.all()[:3] ])+' '+ ', '.join([User.Last_Name for User in self.User.all()[:3] ])
#     get_user.short_description = 'Usuario'

#     def get_email(self):
#         return self.User.Email
#         #', '.join([ User.Email for User in self.User.all()[:3] ])
#     get_email.short_description = 'Email'
class user(models.Model):
    ROL= (
    (1,'admin'),
    (2,'dueño'),
    (3,'evaluador'),
    )
    username= models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=15)
    rol = models.IntegerField(choices=ROL)
    rut = models.CharField(max_length=14)
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=35)