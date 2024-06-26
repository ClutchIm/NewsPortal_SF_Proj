from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Все'
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'time_in': ['gt'],
        }
