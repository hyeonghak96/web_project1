from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Board(models.Model):
    title       = models.CharField(verbose_name='TITLE', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100,
                            blank=True, help_text='simple description text.')
    content     = HTMLField('CONTENTC')                                                    #  models.TextField('CONTENT')
    create_dt   = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt   = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)

    hit         = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
