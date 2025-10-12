
from django import forms


class ArithmeticForm(forms.Form):
    
    number1 = forms.IntegerField()
    number2 = forms.IntegerField()
    