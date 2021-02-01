from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

from photo.fields import ThumbnailImageField
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


class BoardAttachFile(models.Model):
    post            = models.ForeignKey(Post, on_delete=models.CASCADE,
                                        related_name="files",
                                        verbose_name='Post', blank=True, null=True)
    upload_file     = models.FileField(upload_to="%Y/%m/%d",
                                        null=True, blank=True, verbose_name='파일')
    filename        = models.CharField(max_length=64, null=True,
                                        verbose_name='첨부파일명')
    content_type    = models.CharField(max_length=128, null=True,
                                        verbose_name='MIME TYPE')
    size            = models.IntegerField('파일 크기')


    def __str__(self):
        return self.filename

# 장고 실전 9장 포토 이용
class Album(models.Model):
    name = models.CharField('NAME', max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField('IMAGE', upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))