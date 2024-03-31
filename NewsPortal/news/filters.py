import django_filters
from .models import Post, Category
from django import forms

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Название содержит:')
    categories = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Категория:')
    creation_date = django_filters.DateTimeFilter(field_name='creation_date', lookup_expr='gt', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label='Дата новости, позднее:')

    class Meta:
        model = Post
        fields = ['title', 'categories', 'creation_date']

