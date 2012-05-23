from entry.models import Post
from entry.models import Comment
from django.contrib import admin

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    
    inlines = [CommentInline]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'

admin.site.register(Post, PostAdmin)
