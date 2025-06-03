from django import forms
from Home.models import Stocks

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['producto', 'cant_after_Stock']