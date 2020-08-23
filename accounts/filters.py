import django_filters
from django_filters import DateFilter # this class allows to filter by date 
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created',lookup_expr='gte') # date_created is the field we are trying to filter and this field will look for >= 
    end_date = DateFilter(field_name='date_created',lookup_expr='lte')  # similarly will look for <=
    class Meta:
        model = Order
        fields = '__all__'
        exclude=['customer','date_created']


# start_date and end_date is the range given for datefield
# these fields are custom fields in the template and not in the actual Order table

