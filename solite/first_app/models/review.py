from django.db import models


class Review(models.Model):
    image = models.ImageField(upload_to = "upload/images")
    description = models.TextField()
    name = models.CharField(max_length = 100)
    skills = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
    def get_all_reviews():
        return Review.objects.all()
    
    