from django.db import models



class Course(models.Model):
    image = models.ImageField(upload_to = "upload/images")
    book_name = models.CharField(max_length = 100)
    price = models.IntegerField(default = 0)
    original_price = models.IntegerField(default = 0)
    description = models.TextField()
    
    
    def __str__(self):
        return self.book_name
    
    def get_all_course():
        return Course.objects.all()
    
    
    
    
    