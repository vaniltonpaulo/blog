from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import CommentForm

from .models import Post

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date'] 
    context_object_name = 'posts' 

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3] 
        return data


# Helper function used for sorting posts by date
def get_date(post):
    # Returns the 'date' field from a post dictionary
    return post['date']


class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date'] 
    context_object_name = 'all_posts'


class SinglePostView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # Get the default context data from the parent class
        context = super().get_context_data(**kwargs)

        # Get the current post object (the one being viewed)
        current_post = self.get_object()

        # Get all tags associated with this post
        post_tags = current_post.tags.all()
        context['post_tags'] = post_tags
        context['comment_form'] = CommentForm() # Add an empty comment form to the context

        return context

