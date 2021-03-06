from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile = models.CharField(max_length=10, null=True)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
