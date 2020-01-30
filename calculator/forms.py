from django import forms


class CalculatorForm(forms.Form):
    from_currency = forms.CharField(max_length=10, label='From currency')
    to_currency = forms.CharField(max_length=10, label='To currency')
    amount = forms.FloatField(label='Amount')
