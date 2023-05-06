from django.shortcuts import render, redirect #HttpResponseRedirect
from django.views import View
from .models import Customer, Product, Cart, OredrPlaced
from .forms  import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q 
from django.http import JsonResponse

#def home(request):
 #return render(request, 'app/home.html')
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category="TW")
        bottomwears = Product.objects.filter(category='BW')
        mobile = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        return render(request, 'app/home.html',{'topwears':topwears, 'bottomwears':bottomwears, 'mobile':mobile, 'laptop':laptop})
    
    
#def product_detail(request):
 #return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':product})




def add_to_cart(request):
    user= request.user
    product_id = request.GET.get('prod_id')
    product= Product.objects.get(id=product_id)
    #print(product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        #print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount=0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        #print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                amount += tempamount
                totalamount = amount +shipping_amount
            return render(request, 'app/addtocart.html',{'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'app/emptycart.html')
def plus_cart(request):
    if request.method == "GET":
        prod_id= request.GET[prod_id]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount=0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
            totalamount = amount +shipping_amount
        data = {
            'quantity':c. quantity,
            'amount':amount,
            'totalamount':totalamount
            }
    return JsonResponse(data)
    
    



def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add,'active':'btn-primary'})

def orders(request):
    op = OredrPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':op})

#def change_password(request):
 #return render(request, 'app/changepassword.html')



def topwear(request, data=None):
    if data == None:
        topwear = Product.objects.filter(category='TW')
    elif data == 'PUMA': #or data == 'mackbook' or data == 'acer3' or data == 'acer2' or data == 'acer':
        topwear = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
        topwear = Product.objects.filter(category='TW').filter(discounted_price__lt=10000)
    elif data == 'above':
        topwear = Product.objects.filter(category='TW').filter(discounted_price__lt=10000)
    return render(request, 'app/topwear.html', {'topwear':topwear})
    
def bottomwear(request, data=None):
    if data == None:
        bottomwear = Product.objects.filter(category='BW')
    elif data == 'power' or data == 'puma' or data == 'polo' or data == 'jeans' or data == 'Adidas' or data == 'levis':
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'below':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__lt=10000)
    elif data == 'above':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__lt=10000)
    return render(request, 'app/bottomwear.html', {'bottomwear':bottomwear})


def mobile(request, data=None):
    if data == None:
        mobile = Product.objects.filter(category='M')
    elif data == 'POCO' or data == 'Iphone' or data == 'MOTO' or data == 'samsung':
        mobile = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobile = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobile = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobile':mobile})

def laptop(request, data=None):
    if data == None:
        laptop = Product.objects.filter(category='L')
    elif data == 'HP' or data == 'DELL' or data == 'mackbook' or data == 'acer3' or data == 'acer2' or data == 'acer':
        laptop = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptop = Product.objects.filter(category='L').filter(discounted_price__lt=10000)
    elif data == 'above':
        laptop = Product.objects.filter(category='L').filter(discounted_price__lt=10000)
    return render(request, 'app/laptop.html', {'laptop':laptop})


def login(request):
 return render(request, 'app/login.html')

def password_rest(request):
 return render(request, 'app/password_rest.html')


def password_rest_done(request):
 return render(request, 'app/password_rest_done.html')

def password_rest_confirm(request):
 return render(request, 'app/password_rest_confirm.html')

def password_rest_complite(request):
 return render(request, 'app/password_rest_complite.html')



#def login(request):
    #if request.method == "POST":
     #   fm = AuthenticationForm(request=request, data = request.POST)
        #if fm.is_valid():
         #   uname = fm.cleaned_data['username']
        #    upaas =  fm.cleaned_data['password']
       #     user = authenticate(username=uname,  password=upaas)
      #      if user is not None:
     #           login(request, user)
    #            return HttpResponseRedirect('/')
   # else:
    #    fm = AuthenticationForm            
   # fm=AuthenticationForm()
#    return render(request, 'app/login.html',{'form':fm})

#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form} ) 
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "congratukations || Registered Successfully")
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form} ) 
    
            

    

def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount +shipping_amount
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items})

def payment_done(request):
    user = request.user
    custid= request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart= Cart.objects.filter(user=request.user)
    for c in cart:
        OredrPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")



class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm(request. POST)
        return render(request,  'app/profile.html', {'form':form, 'active':'btn-primary'})
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode =form.cleaned_data['zipcode']
            reg=  Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode) 
            #messages.success(request,'Congratulations !! profile Updated successfully')
            messages.success(request, "congratukations || profile Updated  Successfully")
            reg.save()
            
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

#    def post(self, request):
 #       form = CustomerProfileForm(request.POST)
  #      if

    
