from django.urls import path
from super_shop import views

urlpatterns = [
    path('', views.login, name = 'shop-login'),
    path('validate_login/', views.validate_login, name = 'validate_login'),
    path('products/', views.products, name = 'show_products'),
    path('products/<int:catid>', views.products, name = 'show_products_with_id'),
    path('order/', views.order, name = 'shop-order'),

    path('qr', views.qr)
]
