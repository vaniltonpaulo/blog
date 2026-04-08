from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    email_address = models.EmailField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, validators=[MinLengthValidator(10)])
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts')
    tags = models.ManyToManyField(Tag)


