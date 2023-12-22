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

class CalculateGPGPVsForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha inicial")
    end_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha final")
    ignore_locked = forms.BooleanField(required=False, label='Ignorar bloqueados')

class GPVCalculatorForm(forms.Form):
    gp_time = forms.TimeField(widget=forms.TimeInput(format=('%HH:%mm'), attrs={'class': 'form-control', 'type': 'time'}), label="Hora del G.P.")
    mbd_time = forms.TimeField(widget=forms.TimeInput(format=('%HH:%mm'), attrs={'class': 'form-control', 'type': 'time'}), label="Hora del M.B.D.")
    drg_time = forms.TimeField(widget=forms.TimeInput(format=('%HH:%mm'), attrs={'class': 'form-control', 'type': 'time'}), label="Hora del Drg")
    position = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label="Puesto")
    streak = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), label="Racha (en días)")