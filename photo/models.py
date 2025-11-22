from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50) 
    author = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='photos/%Y/%m/%d') 
    description = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title