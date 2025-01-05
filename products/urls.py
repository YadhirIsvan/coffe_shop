
from django.urls import path
from .views import ProductFormView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name="list-product"),
    path('agregar/', ProductFormView.as_view(), name="add-product")
]
