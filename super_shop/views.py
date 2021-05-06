from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import User, Product, Orders
from .view_helper import download_pdf, user_authenticated, category, get_data_by_id, logout
import json

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

    valid_user = user_authenticated(User, phone=phone, email=email)
    
    request.session['uid'] = valid_user.id if valid_user else User.objects.create(name = name, phone=phone, email= email).id
    
    return redirect('show_products')

@category
def products(request, catid = None):
    search_text = ''
    if request.GET:
        search_text = request.GET['search-text']
    
    if catid != None:
        product_data = Product.objects.filter(catid = catid, title__icontains = search_text)
    else:
        product_data = Product.objects.filter(title__icontains = search_text)

    
    data = {'product_data': product_data, 'template': PRODUCT_PAGE,'request': request}
    return data

    # No need to return render. Decorator going take care of this
    # return render(request, PRODUCT_PAGE, data)

def order(request):
    if not request.POST: return

    # Below code for processing only single item

    product_id = request.POST['product-id']
    amount = int(request.POST['amount'])

    product_detail = get_data_by_id(id = product_id, model = Product)
    if not product_detail or amount > product_detail.stock: return
    product_detail.amount = amount
    
    if request.session.get('uid') == None: return
    user = get_data_by_id(id = request.session['uid'], model = User)
    if not user: return

    # order details to be saved in the database
    product_detail_dict = {
        'title': product_detail.title,
        'amount': amount,
        'PPU': product_detail.price,
        'date':'date'
    }
    # save orders
    Orders(userid=user, product_detail=json.dumps(product_detail_dict)).save()

    # update stock
    Product.objects.filter(id = product_detail.id).update(stock = product_detail.stock - amount)

    # passing product_detail as an array to the download_pdf
    # so that download_pdf can calculate total for multiple products
    product_detail = [product_detail]
    return download_pdf(user, product_detail)
