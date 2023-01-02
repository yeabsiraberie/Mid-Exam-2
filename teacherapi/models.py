from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacherName=models.CharField(max_length=200, null=True)
    def __str__(self):
        return ([self.teacherName])