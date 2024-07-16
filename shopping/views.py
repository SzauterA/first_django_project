from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from django.template import loader

# Create your views here.

from .models import Customer, Products

from .forms import CustomerForm, ProductForm, CustomerRegisterForm, ProductUpdateForm

from django.http import HttpResponse

def index(request):
    return render(request, "shopping/index.html")

def page1(request):
    return HttpResponse('Page 1')

def get_customers(request):
    #print(request)
    #print(request.GET)
    #first_name = request.GET.get("first_name") or ""
    #last_name = request.GET.get("last_name") or ""
    #print(first_name)
    customers = Customer.objects.all()
    form = CustomerForm(request.GET or None)
    print(form.is_valid())
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        customers = Customer.objects.filter(
            first_name__icontains=first_name,
            last_name__icontains=last_name,
        )
        if email:
            customers = customers.filter(email=email)
    context = {
        "customers": customers,  
        "form": form,  
    }
    return render(request, "shopping/customers.html", context)

"""
def get_products(request):
    products = Products.objects.all()
    products_str = ''.join(
        [f'<li>{product.name} {product.price}</li>' for product in products]
    )
    return HttpResponse(f'Products:<br>{products_str}')
    """
def get_products(request):
    products = Products.objects.all()
    form = ProductForm(request.GET or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        products = Products.objects.filter(
            name__icontains=name
        )
    context = {
        "products": products,
        "title": "Products:",
        "form": form, 
    }
    return render(request, "shopping/products.html", context)

def get_customer_details(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found", status=404)
    context = {
        "customer": customer,
    }
    return render (request, "shopping/customer_details.html", context)

def get_products_details(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        return HttpResponse("Product not found", status=404)
    
    #product = get_object_or_404(Products, id=product_id)

    context = {
        "product": product,
    }
    return render (request, "shopping/product_details.html", context)

def add_customer(request):
    if request.POST:
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            #customer = (Customer.objects.create(**form.cleaned_data))
            context = {
                'form': CustomerRegisterForm(),
                'success': True,
            }
            #return render(request, "shopping/customer_add.html", context)
            return redirect('customers')
    else:
        form = CustomerRegisterForm()
        context = {
            "form": form
    }
    return render (request, "shopping/customer_add.html", context)

def update_product(request, product_id):
    product = Products.objects.get(id=product_id)
    print(product)  
    if request.POST:
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('product_details', product_id=product_id)  
    else:
        form = ProductUpdateForm(instance=product)
        context = {
            "form": form,
            "product": product
    }
    return render (request, "shopping/product_update.html", context)