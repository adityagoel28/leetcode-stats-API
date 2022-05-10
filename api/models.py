from django.db import models

# Create your models here.

# Create your models here.
class leetcodeUsername(models.Model):
    username = models.CharField(max_length=30)
    count = models.IntegerField(default=1)