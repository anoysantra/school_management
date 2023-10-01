from django.db import models
# Create your models here.

class Subjects(models.Model):
    class_name = models.CharField(max_length=100)
    subjects_name=models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
