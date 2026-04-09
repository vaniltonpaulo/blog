from . import views  # Import all view functions from this app
from django.urls import path  # Used to define URL patterns

# URL patterns for the "blog" app
urlpatterns = [

    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('posts/', views.AllPostsView.as_view(), name='posts-page'),
    # Dynamic route for a single post
    # <slug:slug> captures part of the URL and passes it to the view
    # Example: /posts/my-first-post/
    path('posts/<slug:slug>/', views.SinglePostView.as_view(), name='post-detail-page')
]