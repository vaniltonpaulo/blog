from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.
#superuser: sam
#password: 123456 
#(its a dummy project, you DUMMY, dont use this password in production)
admin.site.register(Author)
admin.site.register(Post)           
admin.site.register(Tag)



