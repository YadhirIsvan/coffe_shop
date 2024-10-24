from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    description = forms.CharField(max_length=300, label='Descripción')  # Cambié 'Description' a minúscula
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')  # Cambié 'Price' a minúscula
    available = forms.BooleanField(initial=True, label='Disponible', required=False)  # Cambié 'Available' a minúscula
    photo = forms.ImageField(label='Foto', required=False)  # Cambié 'Photo' a minúscula

    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],  # Cambié 'Description' a minúscula
            price=self.cleaned_data['price'],  # Cambié 'Price' a minúscula
            available=self.cleaned_data['available'],  # Cambié 'Available' a minúscula
            photo=self.cleaned_data['photo']  # Cambié 'Photo' a minúscula
        )
