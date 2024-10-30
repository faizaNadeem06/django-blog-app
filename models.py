from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    image=models.ImageField(upload_to='photos')

# def __str__(self): ,height_field='None', width_field='None',max_length='None'
#     return self.title + '|' + str(self.author)

# def get_absolute_url(self):
#     return reverse("Detailpost", args=(str(self.id)))






# Create your models here.
