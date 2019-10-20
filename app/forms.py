from django.forms import ModelForm
from .models import Plant, EssentialOil


class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class OilForm(ModelForm):
    class Meta:
        model = EssentialOil
        fields = '__all__'
