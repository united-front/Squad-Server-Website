from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.OneToOneField(User, on_delete=Models.CASCADE)
    steamID = models.CharField(default='',blank=True,max_length=32)
