from .models import User, Category,Product
from django.shortcuts import render,redirect
from django.urls import reverse
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

def logout(request):
    if request.session.get('uid'):
        del request.session['uid']
    return redirect(reverse('shop-login'))

def user_authenticated(phone = '', email = ''):
    if phone.strip() == '' or email.strip() == '':
        return False
    try:
        user = User.objects.get(email = email, phone = phone)
        return user
    except:
        return False

def category(f):
    # Add category list to certain request
    def x(*args, **kwargs):
        allCat = Category.objects.all()
        data = f(*args, **kwargs)
        data['category'] = allCat
        return render(data['request'], data['template'],data)
    return x

def get_product_by_id(product_id):
    try:
        detail = Product.objects.get(id=product_id)
        return detail
    except:
        return False

def get_logged_user_detail(request):
    if request.session.get('uid'):
        user = User.objects.get(id = request.session['uid'])
        return user
    return False

def download_pdf():
    # Copied from https://codeburst.io/django-render-html-to-pdf-41a2b9c41d16
    template = get_template('super_shop/html_pdf.html')
    html = template.render({})
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)