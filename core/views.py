from .models import Product
from django.shortcuts import render
from django.views.generic import View
# Create your views here.
def index(request):

    return render(request,'home-page.html')

class HomePage(View):

    def get(self,request,*args, **kwargs):
        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'home-page.html', context=context)



class ProductDetail(View):

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        print(slug)
        product = Product.objects.filter(slug=slug)
        if product.exists:
            product = product[0]
            context = {
                'product': product
            }
            return render(request, 'product-page.html', context=context) 


    def post(self, request, *args, **kwargs):
        pass