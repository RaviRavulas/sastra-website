from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=25)
    password=models.IntegerField()
    regno=models.IntegerField()
    cgpa=models.IntegerField()
    attendance=models.IntegerField()

    def __str__(self):
        return self.name
