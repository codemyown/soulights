from django.db import models



class ContactUs(models.Model):
    first_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone_no = models.IntegerField(default = 0)
    message = models.TextField()
    
    
    def __str__(self):
        return  self.first_name