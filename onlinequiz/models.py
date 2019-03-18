from django.db import models
from django.urls import reverse
# Create your models here.


class Questions(models.Model):
    question = models.CharField(max_length=255)
    option1  = models.CharField(max_length=255)
    option2  = models.CharField(max_length=255)
    option3  = models.CharField(max_length=255)
    option4  = models.CharField(max_length=255)

    RIGHTOPTIONS = (
        (1, 'Option1'),
        (2, 'Option2'),
        (3, 'Option3'),
        (4, 'Option4'),
    )
    rightop  = models.IntegerField(choices=RIGHTOPTIONS,default="")
    userid   = models.IntegerField()

    def save(self, *args, **kwargs):
        self.userid = 1
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def get_absolute_url(self):
        return reverse('questionlist')



class Movie(models.Model):
    Name = models.CharField(max_length=250)
    Actor = models.CharField(max_length=250)
    Director = models.CharField(max_length=250)


    def get_absolute_url(self):
        return reverse('movielist')







