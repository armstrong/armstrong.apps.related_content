from django.contrib import admin
from .models import Article
from ...admin import RelatedContentInline

class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelatedContentInline]

admin.site.register(Article, ArticleAdmin)
