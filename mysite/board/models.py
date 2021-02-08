from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from account.models import User

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



# 댓글 기능
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (self.author.username if self.author else "무명")+ "의 댓글"


# 게시판 이미지 추가 링크(https://wikidocs.net/91424)
# 댓글 기능 링크 1(https://wikidocs.net/71655)
# 댓글 기능 링크 2(https://fabl1106.github.io/django/2019/05/16/Django-22.-%EC%9E%A5%EA%B3%A0-%EB%8C%93%EA%B8%80-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0(%ED%95%A8%EC%88%98%ED%98%95-%EB%B7%B0).html)
