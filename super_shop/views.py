from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'super_shop/pages/index.html'
    return render(request, template)