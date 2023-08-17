from django import forms

class LinkFkForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha inicial")
    end_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha final")
    ignore_locked = forms.BooleanField(required=False, label='Ignorar bloqueados')
    update_gp = forms.BooleanField(required=False, label="Actualizar G.P.")
    update_mbd_and_drg = forms.BooleanField(required=False, label="Actualizar M.B.D. y Drg")

class CalculateGPPositionsForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha inicial")
    end_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha final")
    ignore_locked = forms.BooleanField(required=False, label='Ignorar bloqueados')
    
class CalculateGPStreaksForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha inicial")
    end_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha final")
    ignore_locked = forms.BooleanField(required=False, label='Ignorar bloqueados')