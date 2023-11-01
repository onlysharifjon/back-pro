from django.db import models




class PasswordModel(models.Model):
    parol = models.CharField(max_length=32)
    user = models.CharField(max_length=16,default='username',unique=True,primary_key=True)

    def __str__(self):
        return self.user
# Create your models here.
