from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class instrouction(models.Model):
    title = models.CharField('TITLE', max_length =100, blank=True)
