from django.urls import path
from order import views
app_name="order"
urlpatterns = [
    path('add_to_cart/<int:pk>/',views.add_to_cart,name="add_to_cart"),

]