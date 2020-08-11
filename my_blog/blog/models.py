from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=324)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=131)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    comment_approved = models.BooleanField(default=False)

    def approve(self):
        self.comment_approved = True
        self.save()


    def __str__(self):
        return self.name
