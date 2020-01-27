from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def main(request):
    content = {
        'products': Product.objects.all(),
    }
    return render(request, 'inventory/list_product.html', content)


def detail_product(request, pk):
    content = {
        'product': Product.objects.get(pk=pk),
    }
    return render(request, 'inventory/detail_product.html', content)


def regist_product(request):
    if request.method == 'GET':
        return render(request, 'inventory/regist_product.html', {
            'sellers': Seller.objects.all()
        })
    elif request.method == 'POST':
        name = request.POST['product_name']
        desc = request.POST['product_desc']
        price = request.POST['product_price']
        stock = request.POST['product_stock']
        # print(request.POST)
        seller_pk = request.POST['product_sell']

        product = Product.objects.create(
            product_name=name,
            product_desc=desc,
            product_price=price,
            product_stock=stock,
            product_sell=Seller.objects.get(pk=seller_pk),
        )

        return redirect('inventory:inventory_main')


def manage_seller(request):
    content = {
        'sellers': Seller.objects.all()
    }
    return render(request, 'inventory/manage_seller.html', content)


def detail_seller(request, pk):
    content = {
        'seller': Seller.objects.get(pk=pk)
    }
    return render(request, 'inventory/detail_seller.html', content)


def regist_seller(request):
    if request.method == 'GET':
        return render(request, 'inventory/regist_seller.html', {})
    elif request.method == 'POST':
        name = request.POST['seller_name']
        phone = request.POST['seller_phone']
        address = request.POST['seller_address']

        seller = Seller.objects.create(
            seller_name=name,
            seller_phone=phone,
            seller_address=address
        )

        return redirect('inventory:manage_seller')


def update_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'GET':
        return render(request, 'inventory/update_product.html', {
            'product': product,
            'sellers': Seller.objects.all()
        })
    if request.method == 'POST':
        name = request.POST['product_name']
        desc = request.POST['product_desc']
        price = request.POST['product_price']
        stock = request.POST['product_stock']
        seller_pk = request.POST['product_sell']

        product.product_name = name
        product.product_desc = desc
        product.product_price = price
        product.product_stock = stock
        product.product_sell = Seller.objects.get(pk=seller_pk)

        product.save()
    return redirect('inventory:detail_product', product.pk)


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'GET':  # url접속만으로 삭제가 되어서는 안됨. 따라서 아무런 작업 X
        return redirect('inventory:detail_product', product.pk)
    elif request.method == 'POST':
        product.delete()
        return redirect('inventory:inventory_main')  # html 만들 필요가 없다!

    return None


def update_seller(request, pk):
    return None


def delete_seller(request, pk):
    seller = Seller.objects.get(pk=pk)

    if request.method == 'GET':  # url접속만으로 삭제가 되어서는 안됨. 따라서 아무런 작업 X
        return redirect('inventory:detail_seller', seller.pk)
    elif request.method == 'POST':
        seller.delete()
        return redirect('inventory:manage_seller')  # html 만들 필요가 없다!
