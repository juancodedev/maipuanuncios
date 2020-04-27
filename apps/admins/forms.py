from django import forms

from apps.home.models import advertisement 

class advertisementForm(forms.ModelForm):
    
    class Meta:
        model = advertisement
        fields = [
            'name',
            'Type_advertisement',
            'Social_network',
            'phones',
            'email',
            'url_website',
            'address',
            'description',
            'image',
            'logo',
            'latitude_longitude',
            'incorporation_date',
            'subscription_type',
            'state',
            'includes_maps',
            'credits_id',
            'open_from',
            'open_to',
        ]
        labels = {
            'name': 'Nombre',
            'Type_advertisement': 'Tipo Aviso',
            'Social_network': 'Red Sociales',
            'phones': 'Telefonos',
            'email': 'Email',
            'url_website': 'Sitio Web',
            'address': 'Direccion',
            'description': 'Descripcion',
            'image': 'Imagen principal',
            'logo': 'Logo Empresa',
            'latitude_longitude':'Ubicacion L/Long',
            'incorporation_date': 'Fecha de inscripcion',
            'subscription_type': 'Tipo subscripcion',
            'state': 'Activo/No-Activo',
            'includes_maps': 'Agregar a Maps',
            'credits_id': 'Creditos disponibles',
            'open_from': 'Abierto desde',
            'open_to':'Cierra a las',
        }
        # widgets = {
        #     'Name': forms.TextInput(attrs={'class':'form-control'}),
        #     'ImageMD': forms.FileInput(attrs={'class':'form-control'}),
        #     'ImageProfile': forms.FileInput(attrs={'class':'form-control'}),
        #     'Address': forms.TextInput(attrs={'class':'form-control'}),
        #     'State_Province': forms.Select(attrs={'class':'form-control'}),
        #     'Phone': forms.TextInput(attrs={'class':'form-control'}),
        #     'Type': forms.Select(attrs={'class':'form-control'}),
        #     'Review': forms.Textarea(attrs={'class':'form-control'}),
        # }