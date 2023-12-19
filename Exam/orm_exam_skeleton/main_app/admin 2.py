from django.contrib import admin
from .models import Author, Article, Review


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_banned')
    list_filter = ('is_banned',)
    search_fields = ('full_name', 'email')


admin.site.register(Author, AuthorAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_on')
    list_filter = ('category',)
    search_fields = ('title',)
    readonly_fields = ('published_on',)


admin.site.register(Article, ArticleAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'rating', 'published_on')
    list_filter = ('rating', 'published_on')
    search_fields = ('article__title',)
    readonly_fields = ('published_on',)


admin.site.register(Review, ReviewAdmin)
