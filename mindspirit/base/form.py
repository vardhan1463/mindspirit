from django.forms import ModelForm
from .models import Room

class RoomForms(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']

        