from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=80)
    Rollno = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.fname}"
    
class meta:
    db_name = "Student"