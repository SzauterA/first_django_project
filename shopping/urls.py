from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page1', views.page1, name='page1'),
    path('customers', views.get_customers, name='customers'),
    path('customers/add/', views.add_customer, name='customer_add'), 
    path("customers/<customer_id>/", views.get_customer_details, name="customer_details"),
    path('products', views.get_products, name='products'),
    path("products/<product_id>/", views.get_products_details, name="product_details"),
    path("products/<product_id>/update", views.update_product, name="product_update")
]