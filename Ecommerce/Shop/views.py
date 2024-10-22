from django.shortcuts import render
from .models import product_model , banner


from django.utils.text import slugify


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
  
        # add logic to add this product to the cart here if user clicks on add to cart button.
       
    
  
  all_products = product_model.objects.all()
  categories = set(product.category for product in all_products) 
  return render(request, 'Shop/lehenga.html', {'categories': categories , 'product':product })
    
  


def product_detail(request , id , a):
 return render(request, 'Shop/productdetail.html')

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

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
