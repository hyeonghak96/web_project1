# Generated by Django 3.1.5 on 2021-02-03 13:49

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('description', models.CharField(blank=True, help_text='simple description text.', max_length=100, verbose_name='DESCRIPTION')),
                ('content', tinymce.models.HTMLField(verbose_name='CONTENTC')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY DATE')),
                ('hit', models.PositiveIntegerField(default=0)),
                ('mainphoto', models.ImageField(blank=True, null=True, upload_to='')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='BoardAttachFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='파일')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
                ('content_type', models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')),
                ('size', models.IntegerField(verbose_name='파일 크기')),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='board.board', verbose_name='Board')),
            ],
        ),
    ]
