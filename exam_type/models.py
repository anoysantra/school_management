from django.db import models

# Create your models here.
class Exams(models.Model):
    exam_name=models.CharField(max_length=20)
    full_marks=models.PositiveIntegerField()

    def __str__(self):
        return self.exam_name