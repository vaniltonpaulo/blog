from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.
#superuser: sam
#password: 123456 
#(its a dummy project, you DUMMY, dont use this password in production)

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author','tags', 'date') 
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {'slug': ('title',)} # Automatically fills the slug field based on the title

admin.site.register(Author)
admin.site.register(Post)           
admin.site.register(Tag)



