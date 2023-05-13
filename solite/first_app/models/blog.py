from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to = "upload/images")
    title = models.CharField(max_length = 100)
    description = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    def get_all_blogs():
        return Blog.objects.all()