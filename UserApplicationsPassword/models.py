from django.db import models

from PasswordManager.models import PasswordModel


class UserApplicationpss(models.Model):
    user_key = models.ForeignKey(PasswordModel, on_delete=models.CASCADE, related_name='user_applicationpss_user_key')
    application = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return str(self.user_key)



# Create your models here.
