# Generated by Django 3.1.6 on 2021-02-09 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG')),
                ('description', models.CharField(blank=True, help_text='simple description text.', max_length=100, verbose_name='DESCRIPTION')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY DATE')),
                ('readcount', models.IntegerField(blank=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'blog_posts',
                'ordering': ('-modify_dt',),
            },
        ),
        migrations.CreateModel(
            name='PostAttachFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='파일')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
                ('content_type', models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')),
                ('size', models.IntegerField(verbose_name='파일 크기')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='blog.post', verbose_name='Post')),
            ],
        ),
    ]
