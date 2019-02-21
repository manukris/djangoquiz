from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.CharField(max_length=255)
    option1  = models.CharField(max_length=255)
    option2  = models.CharField(max_length=255)
    option3  = models.CharField(max_length=255)
    option4  = models.CharField(max_length=255)
    rightop  = models.IntegerField()
    userid   = models.IntegerField()




