import django
from .models import Cart, Product
from django.shortcuts import redirect, render
from django.views.generic import View
# Create your views here.
from .forms import CartForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
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
        product = Product.objects.filter(slug=slug)
        
        if product.exists:
            product = product[0]
            form = CartForm(initial={
                'product': product,
                'user_other': request.user
            })
            context = {
                'product': product,
                'form': form
            }
            return render(request, 'product-page.html', context=context) 


    def post(self, request, *args, **kwargs):
        form = CartForm(request.POST)
        # print(form)
        if form.is_valid():
            cart_exist = Cart.objects.filter(
                product=form.cleaned_data['product'],
                user_other= form.cleaned_data['user_other'],
                )
            if cart_exist.exists():
                cart_exist = cart_exist[0]
                cart_exist.quantity += form.cleaned_data['quantity']
                cart_exist.save()
            else:
                form.save()
            messages.add_message(request,messages.SUCCESS,'Add to cart successfuly')
        else:
            messages.add_message(request,messages.WARNING,'Something !!')
        
        slug = kwargs.get('slug')
        return HttpResponseRedirect(reverse('core:product-detail', kwargs= {
            'slug': slug 
        }))


