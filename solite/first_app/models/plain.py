from django.db import models



class Plain(models.Model):
    plain = models.CharField(max_length = 100)
    price = models.IntegerField(default = 0)
    time = models.CharField(max_length = 100)
    space = models.IntegerField(default = 0)
    transfer = models.IntegerField(default = 0)
    pannel = models.CharField(max_length = 100)
    support = models.IntegerField(default = 0)
    email = models.CharField(max_length  = 100)
    security = models.CharField(max_length = 10)
    
    
    def __str__(self):
        return self.plain
    
    def get_all_plains():
        return Plain.objects.all()