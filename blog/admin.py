from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.
#superuser: sam
#password: 123456 
#(its a dummy project, you DUMMY, dont use this password in production)

# Custom configuration for how the Post model appears in Django admin
class PostAdmin(admin.ModelAdmin):

    # Adds a sidebar filter in the admin panel
    # Allows filtering posts by author, tags, or date
    list_filter = ('author', 'tags', 'date') 

    # Controls which fields are shown in the list view (table)
    # Instead of just showing "Post object", it shows useful info
    list_display = ('title', 'date', 'author')

    # Automatically fills the slug field based on the title
    # When typing the title, Django generates a URL-friendly slug
    # Example: "My First Post" → "my-first-post"
    prepopulated_fields = {'slug': ('title',)}


# Register models so they appear in the admin panel

# Author model → manageable via admin UI
admin.site.register(Author)

# Post model → currently using default admin (NOT PostAdmin yet!)
admin.site.register(Post)

# Tag model → manageable via admin UI
admin.site.register(Tag)


