from django.conf import settings

import aspose.words as convert

import string , random

from .models import SubjectCategory , SubjectItem



letter = random.choice(string.ascii_letters)


'''Запись файла в папку со статикой'''

def file_processing (f , filename):
    with open (f'{settings.BASE_DIR}\\workflow\\static\\workflow\\documents\\{letter}{filename}' , 'wb+') as file:
        for chunk in f.chunks ():
            file.write (chunk)
        return f'{letter}{filename}'


'''Конвертация из DOCX в PDF'''

def convert_to_pdf (file , filename):
    
    doc = convert.Document (f'{settings.BASE_DIR}\\workflow\\static\\workflow\\documents\\{letter}{file}') # type: ignore

    name_file = filename.split('.')[0]

    doc.save (f'{settings.BASE_DIR}\\workflow\\static\\workflow\\documents\\{letter}{name_file}.pdf') # type: ignore
    
    return f'{letter}{name_file}.pdf'


