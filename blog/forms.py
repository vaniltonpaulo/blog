from django import forms
from .models import Comment

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    comment = forms.CharField(widget=forms.Textarea, label='Your Comment')
    class Meta:
        model = Comment
        exclude = ['post']  # We will set the post field in the view, so we exclude it from the form
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'comment': 'Your Comment'
        }