from django.db import models

# Create your models here.
# from django.contrib.auth.models import User

class Instrouction(models.Model):
    title = models.CharField('TITLE', max_length =100, blank=True)


    # owner = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    # auth_user에서 상속받는다


    def __str__(self):
        return self.title

