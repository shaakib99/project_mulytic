from .models import Category
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

def user_authenticated(User, phone = '', email = ''):
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

def get_data_by_id(id = None, model = None):
    if id == None or model == None: return
    try:
        detail = model.objects.get(id=id)
        return detail
    except:
        return False

def download_pdf(user,product_data):
    total = 0
    for x in product_data:
        total += x.amount * x.price

    qr_text = f'name: {user.name} email: {user.email} phone:{user.phone}'

    # Copied from https://codeburst.io/django-render-html-to-pdf-41a2b9c41d16
    template = get_template('super_shop/html_pdf.html')
    html = template.render({'qr_text':qr_text, 'product_data': product_data, 'total': total})
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)
