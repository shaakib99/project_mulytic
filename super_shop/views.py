from django.shortcuts import render,redirect
from .models import User, Product
from .view_helper import user_authenticated

LOGIN_PAGE = 'super_shop/pages/login.html'
PRODUCT_PAGE = 'super_shop/pages/index.html'

def login(request):
    return render(request, LOGIN_PAGE)

def validate_login(request):
    if not request.POST: return

    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']

    if email == '' or phone == '': return # Raise Error

    valid_user = user_authenticated(phone=phone, email=email)
    
    request.session['uid'] = valid_user.id if valid_user else User(name = name, phone=phone, email= email).save().id
    
    return redirect('show_products')

def products(request, catid = None):
    if catid != None:
        product_data = Product.objects.filter(catid = catid)
    else:
        product_data = Product.objects.all()
    
    data = {'product_data': product_data}

    return render(request, PRODUCT_PAGE, data)