from django.shortcuts import render

from django.views.generic import ListView,DetailView
from store.models import Product


# Create your views here.
class HomeListView(ListView):
    model = Product
    template_name='store/index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
	model=Product
	template_name='store/product_details.html'
	context_object_name='product'


# def product_details(request,pk):
# 	product=Product.objects.get(id=pk)
# 	context={
# 		'product':product
# 	}
# 	return render(request,'store/product_details.html',context)
