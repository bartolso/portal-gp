from django import forms
from .models import MBD
from apps.persons.models import Person
from apps.game.mbds.models import MBD
from apps.game.drgs.models import DRG

class Add_mbd(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    message = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Texto del M.B.D.", "class":"form-control"}), label="Mensaje:")
    drg = forms.ModelChoiceField(required=False, queryset=DRG.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), label="Drg:")
    comment = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Comentario:")

    class Meta:
        model = MBD
        exclude = ("valid",)
        fields = '__all__'