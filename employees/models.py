from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=70)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.employee_name