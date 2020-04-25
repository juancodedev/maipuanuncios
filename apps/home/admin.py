from django.contrib import admin
from apps.home.models import advertisement, typeA, social_networks, credits, phones, subscription_plan, NameSocialNetworks
from apps.evaluate.models import Ratings
from apps.admins.models import user, roles
# Register your models here.

# para acceder a la relacion 1 a muchos
# colocamos la clase relacionada en minusculas_set

class advertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_typeName', 'email', 'url_website', 'address', 'description', 'image', 'logo', 'latitude_longitude', 'incorporation_date', 'subscription_type', 'state', 'includes_maps', 'credits_id', 'open_from', 'open_to')
    #list_filter = ('email', 'rating', 'type')

    def get_typeName(self, obj):
        return obj.Type_advertisement.description
        #return ', '.join([ type.description for typedescription in self.type.all()[:3] ])
    # return ', '.join([ User.Email for User in self.User.all()[:3] ])
    get_typeName.short_description = 'Tipo Establecimiento'

    def get_phones(self, obj):
        return obj.phones.Number.all()
    get_phones.shot_description = "Telefonos"


admin.site.register(advertisement, advertisementAdmin)
 
class typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(typeA, typeAdmin)


class social_networksAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_socialNetwork')

admin.site.register(social_networks, social_networksAdmin)


class creditsAdmin(admin.ModelAdmin): 
    list_display = ('id', 'date_recharge', 'amount', 'time_recharge')

admin.site.register(credits, creditsAdmin)

class phonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'typePhone', 'Number', 'wsp' )

admin.site.register(phones, phonesAdmin)

class subscription_planAdmin(admin.ModelAdmin):
     list_display = ('id', 'description', 'amount', 'valid_from', 'valid_to')

admin.site.register(subscription_plan, subscription_planAdmin)

class  rolesAdmin(admin.ModelAdmin):
    list_display = ('id','role', 'description' )

admin.site.register(roles, rolesAdmin)
    
class userAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'password', 'role','email', 'first_name', 'last_name', 'rut' , 'advertisement_id')

admin.site.register(user, userAdmin)

class RatingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'UserRating', 'rating_stars', 'advertisementRating')

admin.site.register(Ratings, RatingsAdmin)

class NameSocialNetworksAdmin(admin.ModelAdmin):
    list_display = ('id','NameDescriptions' )

admin.site.register(NameSocialNetworks, NameSocialNetworksAdmin)
