# Generated by Django 4.1.2 on 2023-01-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectcategory',
            name='image',
            field=models.ImageField(upload_to = 'workflow/static/workflow/img' , verbose_name='Изображение'),
        ),
    ]