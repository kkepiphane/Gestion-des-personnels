import django_filters
from django_filters import DateFilter
from .models import *


class DepenseFilter(django_filters.FilterSet):
    startDays = DateFilter(field_name="date_debut", lookup_expr='get')
    endDays = DateFilter(field_name="date_fin", lookup_expr='get')

    class Meta:
        model = Depense
        fields = ('date_debut', 'date_fin')
        exclude = ['date_debut', 'date_fin']


class RecetteFilter(django_filters.FilterSet):
    startDays = DateFilter(field_name="date_debut", lookup_expr='get')
    endDays = DateFilter(field_name="date_fin", lookup_expr='get')

    class Meta:
        model = Recette
        fields = ('date_debut', 'date_fin')
        exclude = ['date_debut', 'date_fin']
