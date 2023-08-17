from django import forms
from .models import DRG
from apps.persons.models import Person
from apps.game.mbds.models import MBD
from apps.game.drgs.models import DRG

class Add_drg(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    message = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Mensaje (gp por defecto)", "class":"form-control"}), label="")
    mbd = forms.ModelChoiceField(required=False, queryset=MBD.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), label="M.B.D.:")
    comment = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Comentario", "class":"form-control"}), label="")

    class Meta:
        model = DRG
        exclude = ("valid",)
        fields = '__all__'