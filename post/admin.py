from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'user')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'date_posted', 'user')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)