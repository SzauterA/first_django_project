from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Address(models.Model):
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT, related_name='address')

    def __str__(self):
        return f'{self.zip_code} {self.city}, {self.street}'

    class Meta:
        verbose_name_plural = 'Addresses'


class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_discounted = models.BooleanField(default=False)
    expiry_date = models.DateField(null=True, blank=True)
    storage_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
    


class Purchase(models.Model):
    purchase_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='purchases')
    products = models.ManyToManyField(Products, through='PurchaseItem')

    def __str__(self):
        return f'{self.id}  {self.purchase_date}'
    
class PurchaseItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT, related_name='items')
    
    def __str__(self):
        return f'{self.product} {self.quantity} {self.product.price}'