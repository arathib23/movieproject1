from django.db import models

class Movies(models.Model):  #table definition
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    year=models.IntegerField()
    images=models.ImageField(upload_to="details/images",null=True,blank=True)

    def __str__(self):
        return self.name
