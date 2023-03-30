from django import forms
from dynamic_forms.models import FormField

class CycleForm(forms.Form):
    cycle = forms.IntegerField()
    wordbank = forms.BooleanField(initial=False, required=False)
