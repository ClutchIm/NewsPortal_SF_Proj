from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from .models import Author, Category, Post, Comment, PostCategory


class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'title', 'time_in', 'categories', 'genre', 'p_author', 'preview', 'p_rating')
    list_filter = ('time_in', 'category__category', 'p_author')
    search_fields = ('title', 'category__category')

    def categories(self, obj: Post) -> str:
        return ', '.join([category.category for category in obj.category.all()])


class CategoryTransAdmin(TranslationAdmin):
    model = Category


class PostTransAdmin(TranslationAdmin):
    model = Post


# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)
# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
