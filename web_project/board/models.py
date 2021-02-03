from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

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

    mainphoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):              # 현재 데이터의 절대 경로 추출
        return reverse('board:detail', args=(self.id,))

    def get_previous(self):                  # 이전 데이터 추출
        return self.get_previous_by_modify_dt()

    def get_next(self):                      # 다음 데이터 추출
        return self.get_next_by_modify_dt()


class BoardAttachFile(models.Model):
    board            = models.ForeignKey(Board, on_delete=models.CASCADE,
                                        related_name="files",
                                        verbose_name='Board', blank=True, null=True)
    upload_file     = models.FileField(upload_to="%Y/%m/%d",
                                        null=True, blank=True, verbose_name='파일')
    filename        = models.CharField(max_length=64, null=True,
                                        verbose_name='첨부파일명')
    content_type    = models.CharField(max_length=128, null=True,
                                        verbose_name='MIME TYPE')
    size            = models.IntegerField('파일 크기')


    def __str__(self):
        return self.filename



# 자세히 보기 페이지(https://nachwon.github.io/django-12-post-detail/) 참고
