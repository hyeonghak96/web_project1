# Generated by Django 3.1.5 on 2021-02-03 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='slug',
        ),
    ]
