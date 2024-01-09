from django import forms

class ProfetaMessage(forms.Form):
    message = forms.CharField(max_length=10000)