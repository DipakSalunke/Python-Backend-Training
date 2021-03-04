from django.shortcuts import render
from .models import Product
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    print(obj)
    context = {
   'object': obj
    }
    return render (request,"product/detail.html",context)