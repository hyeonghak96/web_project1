from django.db import models

# Create your models here.
# from django.contrib.auth.models import User

class Instrouction(models.Model):
    title = models.CharField('TITLE', max_length =100, blank=True)
    contenthead = models.CharField('CONTENTHEAD', max_length=100, blank=True)
    content = models.TextField('CONTENT', null=True)

    

    def __str__(self):
        return self.title