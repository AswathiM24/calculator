
from django import forms


class ArithmeticForm(forms.Form):
    
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()
    