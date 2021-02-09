from django.db import models
from django.urls import reverse
from account.models import User

# User.interface_set.all  
# User.interface_project_set.all

class Interface(models.Model):
    #  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    performance = models.IntegerField(null=True)
    performance_re = models.IntegerField(null=True)
    writing = models.IntegerField(null=True)
    writing_re= models.IntegerField(null=True)
    attitude =  models.IntegerField(null=True)
    Portfolio = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'interface'
        db_table = 'assessment_interface' # 테이블명 재정의
    
class Interface_project(models.Model):
    #  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    performance = models.IntegerField(null=True)
    performance_re = models.IntegerField(null=True)
    writing = models.IntegerField(null=True)
    writing_re= models.IntegerField(null=True)
    attitude =  models.IntegerField(null=True)
    Portfolio = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'interface_project'
        db_table = 'assessment_interface_project' # 테이블명 재정의

class edge_device(models.Model):
    #  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    performance = models.IntegerField(null=True)
    performance_re = models.IntegerField(null=True)
    writing = models.IntegerField(null=True)
    writing_re= models.IntegerField(null=True)
    attitude =  models.IntegerField(null=True)
    Portfolio = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'edge_device'
        db_table = 'assessment_edge_device' # 테이블명 재정의

class gateway_device(models.Model):
    #  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    performance = models.IntegerField(null=True)
    performance_re = models.IntegerField(null=True)
    writing = models.IntegerField(null=True)
    writing_re= models.IntegerField(null=True)
    attitude =  models.IntegerField(null=True)
    Portfolio = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'gateway_device'
        db_table = 'assessment_gateway_device' # 테이블명 재정의

class iot_project(models.Model):
    #  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    performance = models.IntegerField(null=True)
    performance_re = models.IntegerField(null=True)
    writing = models.IntegerField(null=True)
    writing_re= models.IntegerField(null=True)
    attitude =  models.IntegerField(null=True)
    Portfolio = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'iot_project'
        db_table = 'assessment_iot_project' # 테이블명 재정의

class mix_project(models.Model):
    #  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    performance = models.IntegerField(null=True)
    performance_re = models.IntegerField(null=True)
    writing = models.IntegerField(null=True)
    writing_re= models.IntegerField(null=True)
    attitude =  models.IntegerField(null=True)
    Portfolio = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'mix_project'
        db_table = 'assessment_mix_project' # 테이블명 재정의




class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    # slug = models.SlugField('SLUG', unique=True, allow_unicode=True,help_text='one word for title alias.')
    performance = models.IntegerField(null=True)
    performance_re = models.IntegerField(null=True)
    writing = models.IntegerField(null=True)
    writing_re= models.IntegerField(null=True)
    attitude =  models.IntegerField(null=True)
    Portfolio = models.IntegerField(null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'assessment_posts' # 테이블명 재정의
        ordering = ('-modify_dt',) # orderby 절, -이면 내림차순

    def __str__(self):
        return self.title
    # def get_absolute_url(self): # 현재 데이터의 절대 경로 추출
    # return  reverse('assessment:post_detail', args=(self.slug,))
    def get_previous(self): # 이전 데이터 추출
        return self.get_previous_by_modify_dt()
    def get_next(self): # 다음 데이터 추출
        return self.get_next_by_modify_dt()
