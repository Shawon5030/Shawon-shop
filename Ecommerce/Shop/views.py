from django.shortcuts import render
from .models import product_model , banner




def plus_cart(request):
  id = request.GET.get('prod_id')
  print(id)
  
  product_id = Cart_model.objects.get(Q(products=id) & Q(user=request.user))
  if product_id is not None:
     product_id.quantity += 1
     product_id.save()

     if request.user.is_authenticated:
          p = [p for p in Cart_model.objects.all() if p.user == request.user]
          
          amount = 0
          for p in p:
               amount += p.products.decounted_price * p.quantity

          total_amount = amount + 100
          data = {
            
            'amount': amount,
            'totalamount': total_amount,
            'quantity': p.quantity
          }
          return JsonResponse(data)
def minus_cart(request):
  id = request.GET.get('prod_id')
  print(id)

  
  product_id = Cart_model.objects.get(Q(products=id) and Q(user=request.user))
  if product_id is not None:
     product_id.quantity =product_id.quantity- 1
     product_id.save()
     print("Product")

     if request.user.is_authenticated:
          p = [p for p in Cart_model.objects.all() if p.user == request.user]
          
          amount = 0
          for p in p:
               amount += p.products.decounted_price * p.quantity

          total_amount = amount + 100
          data = {
            
            'amount': amount,
            'totalamount': total_amount,
            'quantity': p.quantity
          }
          return JsonResponse(data)
def remove_cart(request):
     id = request.GET.get('prod_id')
     print(id)

     
     product_id = Cart_model.objects.get(Q(products=id) and Q(user=request.user))
     print(product_id)
     
          
     product_id.delete()


     p = [p for p in Cart_model.objects.all() if p.user == request.user]

     amount = 0
     for p in p:
          amount += p.products.decounted_price * p.quantity

     total_amount = amount + 100
     data = {
          
          'amount': amount,
          'totalamount': total_amount,
          
     }
     return JsonResponse(data)
          


# Create your views here.
def home(request):
     banners = banner.objects.all()
     all = product_model.objects.all()
     return render(request, 'Shop/home.html' , {'banners':banners , 'all':all})

def lehenga(request):
    all_products = product_model.objects.all()
    categories = set(product.category for product in all_products) 
    print(categories)
    women = product_model.objects.filter(category='w')
    baby = product_model.objects.filter(category='b') # Extract unique categories
    return render(request, 'Shop/lehenga.html', {'categories': categories})

def shop_show(request, i):
  product = product_model.objects.filter(category=i)
  print(product)
  all_products = product_model.objects.all()
  categories = set(product.category for product in all_products) 
  return render(request, 'Shop/lehenga.html', {'categories': categories , 'product':product })
    
  


def product_detail(request , id , a):
 product = product_model.objects.get(id=id)
 
 return render(request, 'Shop/productdetail.html' , {'product': product})


from .models import *

from django.http import HttpResponseRedirect
from  django.shortcuts import redirect

def add_to_cart(request):
 product_id = request.GET.get('product_id')
 print(product_id)
 product_id = product_model.objects.get(id=product_id)
 print(product_id)
 Cart_model(products=product_id , user=request.user).save()
 return  redirect('show-cart')

def show_cart(request):
  cart = Cart_model.objects.filter(user=request.user)
  if request.user.is_authenticated:
    p = [p for p in Cart_model.objects.all() if p.user == request.user]
    print(p)
    amount = 0
    for p in p:
      amount += p.products.decounted_price * p.products.quantity

    total_amount = amount + 100
    print(total_amount, amount)
  return render(request, 'Shop/addtocart.html', {'cart': cart , 'amount': amount, 'total_amount': total_amount})

from django.db.models import Q
from django.http import JsonResponse




  


def buy_now(request):
 return render(request, 'Shop/buynow.html')

def profile(request):
 return render(request, 'Shop/profile.html')

def address(request):
 return render(request, 'Shop/address.html')

def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')



def login(request):
     return render(request, 'Shop/login.html')

def customerregistration(request):
 return render(request, 'Shop/customerregistration.html')

def checkout(request):
 return render(request, 'Shop/checkout.html')
