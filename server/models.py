from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True , null=True)
    def __str__(self):
        return self.name
class Servers(models.Model):
    name=models.CharField(max_length=100)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='server_owner')
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='server_category')
    description=models.CharField(max_length=255, blank=True)
    memebers=models.ManyToManyField(settings.AUTH_USER_MODEL)

class Channels(models.Model):
    name=models.CharField(max_length=100)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='channel_owner')
    topic=models.CharField(max_length=100)
    server=models.ForeignKey(Servers,on_delete=models.CASCADE,related_name='channel_owner')
    
    def save(self, *args,**kwargs):
        self.name=self.name.lower()
        return super(Channels,self).save(*args,**kwargs)    
    
    def __str__(self):
        return self.name
    
    