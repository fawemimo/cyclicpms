from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils import timezone
# from PIL import Image

from accounts.models import User
from directors.models import Director


class Post(models.Model):
    director            = models.ForeignKey(Director,on_delete=models.CASCADE,blank=True,null=True)
    title               = models.CharField(max_length=100)
    content             = RichTextField(blank=True,null=True)
    # video               = models.FileField(upload_to='media/',default=' ',blank=True,null=True)
    # thumbnail           = models.FileField(upload_to='media/',blank=True,null=True)
    # image               = models.FileField(default='unsplash.jpg',upload_to = "media/")
    date_posted         = models.DateTimeField(auto_now_add=True)
    author              = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    
    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 1000 or img.width > 1000:
    #         output_size = (1000, 1000)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
            
    class Meta:
        db_table = 'posts'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'   
