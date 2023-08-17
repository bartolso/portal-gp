from django import forms
from .models import GP
from apps.game.mbds.models import MBD
from apps.persons.models import Person

class Add_gp(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), label="Jugador")
    date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha")
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), label="Hora")
    mbd = forms.ModelChoiceField(required=False, queryset=MBD.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), label="M.B.D.")
    valid = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Opciones: Si, No", "class":"form-control"}), label="Validez")
    message = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "gp (por defecto)", "class":"form-control"}), label="Mensaje")
    comment = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Comentarios")

    class Meta:
        model = GP
        exclude = ("position", "streak", "gpv")
        fields = '__all__'