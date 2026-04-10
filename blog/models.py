from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

# Model representing a tag (e.g. "Python", "Django")
class Tag(models.Model):

    # Short label for the tag
    caption = models.CharField(max_length=20)

    def __str__(self):
        # Controls how the tag is displayed (admin, shell, etc.)
        return self.caption



# Model representing an author of posts
class Author(models.Model):

    # Author's first name
    first_name = models.CharField(max_length=100)

    # Author's last name
    last_name = models.CharField(max_length=100) 

    # Email must be unique (no two authors can share it)
    email_address = models.EmailField(unique=True)

    def fullname(self):
        # Helper method to combine first + last name
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        # Display full name in admin instead of "Author object"
        return self.fullname()



# Model representing a blog post
class Post(models.Model):

    # Title of the post
    title = models.CharField(max_length=150)

    # Short summary shown in previews
    excerpt = models.CharField(max_length=300)


    image_name = models.ImageField(upload_to='posts', null=True) # Optional image field; uploaded files go to MEDIA_ROOT/posts/

    # Automatically updates to current date every time the post is saved
    date = models.DateField(auto_now=True)

    # URL-friendly identifier for the post
    # Must be unique and at least 10 characters long
    slug = models.SlugField(
        unique=True,
        validators=[MinLengthValidator(10)]
    )

    # Full content of the post
    content = models.TextField()

    # Relationship: many posts → one author
    # If author is deleted, set this field to NULL
    # related_name='posts' allows: author.posts.all()
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True
    )

    # Relationship: many posts ↔ many tags
    # A post can have multiple tags, and a tag can belong to multiple posts
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):

    # Name of the person who wrote the comment
    user_name = models.CharField(max_length=100)

    user_email = models.EmailField() # Email of the commenter
    # The comment text
    text = models.TextField(max_length=500)

    # Date when the comment was created; set automatically on creation
    date = models.DateTimeField(auto_now_add=True)

    # Relationship: many comments → one post
    # If the post is deleted, delete all its comments as well
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.user_name} - {self.post.title}"