
import os
from crypt import methods
from types import MethodType
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from playground.test import print_file
from store.models import Product, Customer, Order, OrderItem, Address, Cart, CartItem, Collection, Promotion


def calculate():
    x = 1
    y = 2
    return x + y


def say_hello(request):
    x = calculate()
    path = '/Volumes/Extras/The Ultimate Django Series/'
    q = list()
    q.append(path)
    #files = print_file(q) 
    products = Product.objects.prefetch_related('promotions').all()
    orders = Order.objects.select_related('customer').all()

    rendered_template = render(request, 'hello.html', {'name': 'World', 'products': products, 'orders': orders})
    return rendered_template

