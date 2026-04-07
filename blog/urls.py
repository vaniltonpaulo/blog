from . import views  # Import all view functions from this app
from django.urls import path  # Used to define URL patterns

# URL patterns for the "blog" app
urlpatterns = [

    # Homepage route
    # When user visits "" (root URL), call starting_page view
    # name='starting-page' allows referencing this URL in templates
    path('', views.starting_page, name='starting-page'),

    # Route for all posts
    # Example: /posts/
    path('posts/', views.posts, name='posts-page'),

    # Dynamic route for a single post
    # <slug:slug> captures part of the URL and passes it to the view
    # Example: /posts/my-first-post/
    path('posts/<slug:slug>/', views.post_detail, name='post-detail-page')
]