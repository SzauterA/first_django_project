from django.contrib.admin import SimpleListFilter
from django.db import models


class GenericIntegerRangeFilter(SimpleListFilter):
    title = 'Integer range'
    parameter_name = None
    field_name = None
    step = 100

    def lookups(self, request, model_admin):
        if not self.field_name:
            return []

        queryset = model_admin.get_queryset(request)
        min_value = queryset.aggregate(min_value=models.Min(self.field_name))['min_value']
        max_value = queryset.aggregate(max_value=models.Max(self.field_name))['max_value']

        lookups = []
        for start in range(min_value, max_value + 1, self.step):
            end = start + self.step - 1
            lookup_value = f"{start}-{end}"
            lookup_label = f"{start} to {end}"
            lookups.append((lookup_value, lookup_label))

        return lookups

    def queryset(self, request, queryset):
        if not self.field_name:
            return queryset

        if self.value():
            start = self.value().split('-')[0]
            end = self.value().split('-')[1]
            filter_kwargs = {
                f'{self.field_name}__gte': start,
                f'{self.field_name}__lte': end
            }
            return queryset.filter(**filter_kwargs)
        return queryset


class PriceRangeFilter(GenericIntegerRangeFilter):
    title = 'Price range'
    parameter_name = 'price_range2'
    field_name = 'price'


class QuantityRangeFilter(GenericIntegerRangeFilter):
    title = 'Quantity range'
    parameter_name = 'quantity_range'
    field_name = 'quantity'

"""
class IntegerRangeFilter(SimpleListFilter):
    title = 'Price range'
    parameter_name = 'price_range2'

    def lookups(self, request, model_admin):
        queryset = model_admin.get_queryset(request)
        min_value = min(queryset, key=lambda x: x.price).price
        max_value = max(queryset, key=lambda x: x.price).price
        # min_value = queryset.aggregate(min_value=models.Min('price'))['min_value']
        # max_value = queryset.aggregate(max_value=models.Max('price'))['max_value']
        step = 50

        lookups = []
        for start in range(min_value, max_value + 1, step):
            end = start + step - 1
            lookup_value = f"{start}-{end}"
            lookup_label = f"{start} to {end}"
            lookups.append((lookup_value, lookup_label))

        return lookups

    def queryset(self, request, queryset):
        if self.value():
            start = self.value().split('-')[0]
            end = self.value().split('-')[1]
            return queryset.filter(price__gte=start, price__lte=end)
        return queryset
"""

class GenericIntegerRangeFilter(SimpleListFilter):
    title = 'Integer range'
    parameter_name = None
    field_name = None
    step = 100

    def lookups(self, request, model_admin):
        if not self.field_name:
            return []

        queryset = model_admin.get_queryset(request)
        min_value = queryset.aggregate(min_value=models.Min(self.field_name))['min_value']
        max_value = queryset.aggregate(max_value=models.Max(self.field_name))['max_value']

        lookups = []
        for start in range(min_value, max_value + 1, self.step):
            end = start + self.step - 1
            lookup_value = f"{start}-{end}"
            lookup_label = f"{start} to {end}"
            lookups.append((lookup_value, lookup_label))

        return lookups

    def queryset(self, request, queryset):
        if not self.field_name:
            return queryset

        if self.value():
            start = self.value().split('-')[0]
            end = self.value().split('-')[1]
            filter_kwargs = {
                f'{self.field_name}__gte': start,
                f'{self.field_name}__lte': end
            }
            return queryset.filter(**filter_kwargs)
        return queryset


class PriceRangeFilter(GenericIntegerRangeFilter):
    title = 'Price range'
    parameter_name = 'price_range2'
    field_name = 'price'


class QuantityRangeFilter(GenericIntegerRangeFilter):
    title = 'Quantity range'
    parameter_name = 'quantity_range'
    field_name = 'quantity'
 

