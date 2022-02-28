from django.contrib import admin
from .models import Article, Comment

# StackedInline
# class CommentInline(admin.StackedInline):
#     model = Comment
#     # default it's shows 3 extra comment
#     extra = 0

# TabularInline
class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)