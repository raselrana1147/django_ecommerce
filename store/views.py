from django.shortcuts import render

from django.views.generic import ListView, DetailView
from store.models import Product, ProductImage


# Create your views here.
class HomeListView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImage.objects.filter(product=self.object.id)
        return context

