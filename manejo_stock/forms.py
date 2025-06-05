from django import forms
from Home.models import Stocks

class StocksForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = '__all__'
