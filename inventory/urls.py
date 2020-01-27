from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [

    path('', views.main, name='inventory_main'),
    path('product/<int:pk>/', views.detail_product, name='detail_product'),
    path('product/regist/', views.regist_product, name='regist_product'),
    path('product/update/<int:pk>/', views.update_product, name='update_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),

    path('seller/', views.manage_seller, name='manage_seller'),
    path('seller/<int:pk>/', views.detail_seller, name='detail_seller'),
    path('seller/regist/', views.regist_seller, name='regist_seller'),
    path('seller/update/<int:pk>/', views.update_seller, name='update_seller'),
    path('seller/delete/<int:pk>/', views.delete_seller, name='delete_seller'),

]
