from django.contrib import admin

class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price Range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('1', '100-200'),
            ('2', '200-300'),
            ('3', '300-400'),
            ('4', '400 <')
        )
    
    def queryset(self, request, queryset):
        print(self.value())
        if self.value() == '1':
            queryset = queryset.filter(price__gte=100, price__lte=200)
        if self.value() == '2': 
            queryset = queryset.filter(price__gte=200, price__lte=300)
        if self.value() == '3':
            queryset = queryset.filter(price__gte=300, price__lte=400)
        if self.value() == '4': 
            queryset = queryset.filter(price__gte=400)

        return queryset
        
class CustomerFilterByAge(admin.SimpleListFilter):
    title = 'Age'
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return (
            ('1', '0-10'),
            ('2', '11-20'),
            ('3', '21-30'),
            ('4', '30-40'),
            ('5', '40 <')
        )
    
    def queryset(self, request, queryset):
        print(self.value())
        if self.value() == '1':
            queryset = queryset.filter(age__gte=0, age__lte=20)
        if self.value() == '2': 
            queryset = queryset.filter(age__gte=21, age__lte=40)
        if self.value() == '3':
            queryset = queryset.filter(age__gte=41, age__lte=60)
        if self.value() == '4': 
            queryset = queryset.filter(age__gte=61)

        return queryset