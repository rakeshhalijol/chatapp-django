from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Detial(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    msg = models.TextField()

    def __str__(self):
        return f"{self.user}"