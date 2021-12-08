from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug',
                    'status', 'date_posted', 'author', 'post_category')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('description',)}


# These are the models I have registered
admin.site.register(Post, PostAdmin)
