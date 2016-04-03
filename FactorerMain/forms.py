from django import forms
from django.core.validators import RegexValidator


class AlgorithmInputForm(forms.Form):
    number = forms.CharField(validators=[RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')])
