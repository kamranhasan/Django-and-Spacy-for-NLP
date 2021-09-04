from django.db import models

# Create your models here.
class Input(models.Model):
    sentence=models.CharField(max_length=2000,default='')
    document = models.FileField(upload_to='documents/', null=True, blank=True)

class Customized(models.Model):
    key=models.CharField(max_length=2000,default='')
    value=models.CharField(max_length=2000,default='')
    def __str__(self):
        return self.key + " replace with " + self.value
        