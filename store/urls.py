from django.urls import path
from store import views
app_name="store"
urlpatterns = [
    path('',views.HomeListView.as_view(),name="home"),
    path('product_details/<int:pk>/',views.ProductDetailView.as_view(),name="product_details"),
]
