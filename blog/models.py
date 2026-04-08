from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, validators=[MinLengthValidator(10)])
    content = models.TextField()
    # image = models.CharField(max_length=100)
    # author = models.CharField(max_length=50)


