from django.db import models
from django.urls import reverse 




class SubjectCategory (models.Model):
    title = models.CharField (max_length = 50 , verbose_name = 'Название предмета')
    full_title = models.CharField (max_length = 150 , blank = True , verbose_name = 'Полное название')
    slug = models.SlugField (max_length = 30 , unique = True , db_index = True , verbose_name = 'URL Предмета')
    image = models.ImageField (upload_to = 'workflow/static/workflow/img' , verbose_name = "Изображение")

    def __str__ (self):
        return self.title

    class Meta:
        verbose_name = ('Категория предмета')
        verbose_name_plural = ('Категории предметов')

    def get_absolute_url (self):
        return reverse ('choiced_subject_category' , kwargs = {'category_slug': self.slug})

    

class SubjectItem (models.Model):
    title = models.CharField (max_length = 180 , verbose_name = 'Название работы')
    theme = models.CharField (max_length = 200 , blank = True , verbose_name = 'Тема')
    docx_file = models.FileField (verbose_name = 'Docx Файл')
    pdf_file = models.FileField (verbose_name = 'PDF Файл')
    video = models.FileField (blank = True , verbose_name = 'Видео')
    author = models.CharField (max_length = 30 , blank = True , verbose_name = 'Имя Автора')
    note = models.TextField (max_length = 1000 , blank = True , verbose_name = 'Примечание')
    slug = models.SlugField (max_length = 40 , unique = True , db_index = True , verbose_name = 'URL Работы')

    category = models.ForeignKey ('SubjectCategory' , on_delete = models.PROTECT , null = True , verbose_name = 'Предмет')

    def __str__ (self):
        return self.title

    class Meta:
        verbose_name = 'Практическая/Лабораторная'
        verbose_name_plural = 'Практические/Лабораторные'

    def get_absolute_url (self):
        return reverse ('subject_item' , kwargs = {'subject_item_slug': self.slug})

    def get_absolute_url_edit_task (self):
        return reverse ('edit_task' , kwargs = {'subject_item_slug': self.slug})







