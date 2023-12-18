from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_products, name="index"),
    path("add", views.add_product, name="add"),
]
