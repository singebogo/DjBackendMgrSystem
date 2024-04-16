import django_filters
from django.db.models import Q
from .models import DataDict
from django_filters.views import FilterView
from .tables import DataDictTable

class DataDictFilter(django_filters.FilterSet):
    '''
    Filter user by username, email, is_staff, ect
    '''
    # 自定义过滤字段
    query = django_filters.CharFilter(method='my_custom_filter', label='关键词')


    def my_custom_filter(self, queryset, q, value):
        return queryset.filter(Q(username__icontains=value) | Q(email__icontains=value))


    class Meta:
        # 使用哪个模型和哪些字段过滤
        model = DataDict
        fields = {
            'type',
            'code',
            'invildId'
        }

# from django_filters import FilterSet
# from .models import DataDict
#
# class DataDictFilter(FilterSet):
#     class Meta:
#         model = DataDict
#         fields = {"name": ["exact", "contains"], "code": ["exact"]}