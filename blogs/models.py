from email.policy import default
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils import timezone

# from PIL import Image

from accounts.models import User
from directors.models import Director


class PostObjects(models.Manager):
    """
    CUSTOM POST OBJECTS MANAGER
    """

    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    """
    BLOG POST MODEL
    """

    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    # video               = models.FileField(upload_to='media/',default=' ',blank=True,null=True)
    # thumbnail           = models.FileField(upload_to='media/',blank=True,null=True)
    # image               = models.FileField(default='unsplash.jpg',upload_to = "media/")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique_for_date="published",blank=True,null=True)

    options = (("draft", "Draft"), ("published", "Published"))
    status = models.CharField(max_length=50, choices=options, default="published")
    objects = models.Manager()
    postobjects = PostObjects()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 1000 or img.width > 1000:
    #         output_size = (1000, 1000)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    class Meta:
        ordering = ("-published",)
        verbose_name = "Post"
        verbose_name_plural = "Posts"
