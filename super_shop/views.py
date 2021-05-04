from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import User, Product, Orders
from .view_helper import download_pdf, user_authenticated, category, get_product_by_id, get_logged_user_detail, logout

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
    return download_pdf()
    if not request.POST: return

    product_id = request.POST['product-id']
    amount = int(request.POST['amount'])

    product_detail = get_product_by_id(product_id)
    if not product_detail or amount > product_detail.stock: return

    user = get_logged_user_detail(request)
    if not user: return
    # save orders
    Orders(userid=user, productid=product_detail,amount = amount).save()

    # update stock
    Product.objects.filter(id = product_detail.id).update(stock = product_detail.stock - amount)

    return HttpResponse('Done')

def qr(request):
    return render(request, 'super_shop/html_pdf.html')