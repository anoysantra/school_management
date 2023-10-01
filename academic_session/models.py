from django.db import models

# Create your models here.
class AcademicSession(models.Model):
    session_name = models.CharField(max_length=100)
    start_date= models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.session_name