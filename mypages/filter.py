import django_filters
from .models import Vocab, VocabularySets
from django_filters import CharFilter

class SetSearch(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = VocabularySets
        fields = '__all__'
        exclude = ['username', 'slug']

class FilterSearch(django_filters.FilterSet):
    word = CharFilter(field_name='word', lookup_expr='icontains')
    class Meta:
        model = Vocab
        fields = '__all__'
        exclude = ['title', 'eng', 'p', 'star']