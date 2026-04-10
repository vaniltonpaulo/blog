from django import forms
from .models import Comment

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        exclude = ['post']  # We will set the post field in the view, so we exclude it from the form
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'comment': 'Your Comment'
        }