from django.db import models

# Create your models here.
class Student(models.Model):
    studentName=models.CharField(max_length=200)
    def __str__(self):
        return ([self.studentName])