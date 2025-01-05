
from django.views import generic
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product

class ProductFormView(generic.FormView):
    template_name = "productos.html"
    form_class = ProductForm
    success_url = reverse_lazy('add-product')
 
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    model = Product
    template_name = 'lista_productos.html'
    context_object_name = 'prodd'

