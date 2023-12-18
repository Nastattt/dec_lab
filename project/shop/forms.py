from django import forms

from shop.models import Product


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
            'description': forms.Textarea(attrs={'class': 'description'}),
            'price': forms.NumberInput(attrs={'class': 'price'}),
        }
