from sorl.thumbnail import ImageField
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name


class Video(models.Model):
    video = models.FileField(upload_to='media/')
    video_name = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.video_name


class Comment(models.Model):
    video_name = models.ForeignKey(Video, related_name="comments", on_delete=models.CASCADE,)
    comment = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video.video_name



# Create your models here.
