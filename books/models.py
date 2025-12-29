from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200);
    subtitle = models.CharField(max_length=300);
    author = models.CharField(max_length=200);
    price = models.DecimalField(max_digits=20 , decimal_places=2)
    
    def  __str__(self):
        return self.title
    
    

# Create your models here.
