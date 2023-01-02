from django.db import models

class Employe(models.Model):
    employeName=models.CharField(max_length=200, null=True)
    def __str__(self):
        return ([self.employeName])
