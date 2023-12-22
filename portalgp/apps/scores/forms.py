from django import forms

class ScoresCalculatorForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha inicial")
    end_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), label="Fecha final")