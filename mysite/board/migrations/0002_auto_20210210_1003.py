# Generated by Django 3.1.5 on 2021-02-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y%m%d'),
        ),
    ]