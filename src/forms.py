from django.forms import ModelForm
from .models import tarea


class tareaform(ModelForm):
    class Meta:
        model = tarea
        fields = ['title','description','datecompleted','important']
        
