from django.shortcuts import render , get_object_or_404

from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect 
from django.urls import reverse

from .models import SubjectCategory , SubjectItem

from .extra_functions import file_processing , convert_to_pdf 
                            
from transliterate import slugify
import string , random




@login_required
def subject_category (request):

    categories = SubjectCategory.objects.all()
    subject = SubjectItem.objects.all()

    context = {
        'categories': categories , 
        'subject_items': subject ,
    }

    if request.method == 'POST':

        if request.POST ["title"] == "" :
            return render (request, 'workflow/workflow_page.html', context = {'categories': categories , 'subject_items': subject , 'error': 'Отсутсвует название'})

        # Перевод слага с русского на eng
        en_slug = slugify (request.POST ["title"]) 

        if en_slug == None :
            return render (request, 'workflow/workflow_page.html', context = {'categories': categories , 'subject_items': subject , 'error':'Неправильный язык'})

        # Категория предмета
        item_category = SubjectCategory.objects.get (title = request.POST ["category-item"]) 

        if request.FILES == {} :
            return render (request, 'workflow/workflow_page.html', context = {'categories': categories , 'subject_items': subject , 'error': 'Файл обязателен'})

        else:

            # Достает имя файла
            file_name = request.FILES['file'].name 

            # Возвращает имя DOCX , загружает файл в директорию
            file_process = file_processing ( f = request.FILES ['file'] , filename = file_name) 

            # Конвертация и сохранение в PDF 
            convert_pdf = convert_to_pdf (file = file_name , filename = file_name) 
            
            item = SubjectItem.objects.create ( author = request.user.username , title = request.POST ["title"] , theme = request.POST ["theme"],\

                                                docx_file = file_process , pdf_file = convert_pdf , note = request.POST["note"] ,\

                                                slug = f'{en_slug}{random.choice(string.ascii_letters)}' , category = item_category )
            item.save()
            
        return redirect (f'task/{item.slug}/')
    
    else:     
        return render (request , 'workflow/workflow_page.html' , context = context)
        


@login_required
def choiced_subject_category (request , category_slug):
    
    category = get_object_or_404 (SubjectCategory , slug = category_slug)
    subject = SubjectItem.objects.filter (category_id = category.pk)    
    
    context = {
        'category': category ,
        'subject': subject ,
    }

    return render (request , 'workflow/workflow_choiced_subject_category.html' , context = context)



@login_required
def subject_item (request , subject_item_slug):

    subject = SubjectItem.objects.get (slug = subject_item_slug) 

    category = SubjectCategory.objects.all()

    context = {
        'subject': subject , 
        'category': category ,
    }

    if request.method == 'POST':

        if request.POST ["title"] == "" :
            return render (request, 'workflow/workflow_subject_item.html', context = {'category': category , 'subject': subject , 'error': 'Отсутсвует название'})

        # Перевод слага с русского на eng
        en_slug = slugify (request.POST ["title"]) 

        if en_slug == None :
            return render (request, 'workflow/workflow_subject_item.html', context = {'category': category , 'subject': subject , 'error':'Неправильный язык'})

        else:
            
            # Категория предмета
            item_category = SubjectCategory.objects.get (title = request.POST ["category-item"]) 

            if request.FILES == {} :
                
                SubjectItem.objects.filter (slug = subject_item_slug).update ( author = request.user.username , title = request.POST ["title"] ,\

                                                                               note = request.POST["note"] , category = item_category )
            else :

                # Достает имя файла
                file_name = request.FILES['file'].name 

                # Возвращает имя DOCX , загружает файл в директорию
                file_process = file_processing ( f = request.FILES ['file'] , filename = file_name) 

                # Конвертация и сохранение в PDF 
                convert_pdf = convert_to_pdf (file = file_name , filename = file_name) 
                
                # Обновление записи в DB
                SubjectItem.objects.filter (slug = subject_item_slug).update ( author = request.user.username , title = request.POST ["title"] ,\

                                                                               docx_file = file_process , pdf_file = convert_pdf ,\

                                                                               note = request.POST["note"] ,category = item_category )

                # Добавление в контекст subject + category для корректного рендера
                subject = SubjectItem.objects.get (slug = subject_item_slug)

                category = SubjectCategory.objects.all()

                return render (request , 'workflow/workflow_subject_item.html' , {'subject': subject , 'category': category }) 

    return render (request , 'workflow/workflow_subject_item.html' , context)



                                                                                     


