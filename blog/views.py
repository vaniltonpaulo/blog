from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CommentForm
from .models import Post


# Homepage view (shows latest 3 posts)
class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


# All posts page
class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


# Single post view (GET + POST for comments)
class SinglePostView(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id')  # newest first
        }

        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            # Create comment object but don't save to DB yet
            comment = comment_form.save(commit=False)

            # Attach post to the comment
            comment.post = post

            # Now save to database
            comment.save()

            # Redirect to avoid form resubmission
            return HttpResponseRedirect(
                reverse('post-detail-page', args=[slug])
            )

        # If form is invalid, re-render page with errors
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,  # IMPORTANT: keep user input + errors
            'comments': post.comments.all().order_by('-id')
        }

        return render(request, 'blog/post-detail.html', context)