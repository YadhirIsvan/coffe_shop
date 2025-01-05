from django.shortcuts import render

from django.views.generic import DetailView
# Create your views here.

from .models import Order

class MyOrderView(DetailView):
    model = Order
    template_name = "my_order.html"
    context_object_name = "order"

    def get_object(self, queryset =None):
        return Order.objects.filter(is_active=True ).first()