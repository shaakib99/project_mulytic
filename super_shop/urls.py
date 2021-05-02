from django.urls import path
from super_shop import views

urlpatterns = [
    path('',views.index,name='shop-home')
]
