from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout

from django.db import IntegrityError


def signup_user (request):

    if request.method == 'GET':
        
        if request.user.is_authenticated:
            return redirect ('home')
        else:
            return render ( request , 'linker/main_page.html' )

    if request.method == 'POST':

        if request.POST ["password1"] == request.POST ["password2"]:
            try:
                user = User.objects.create_user ( username = request.POST ["username"] , password = request.POST ["password1"] )
                user.save()
                login (request , user)
                return redirect ('home')
                
            except IntegrityError:
                return render ( request , 'linker/main_page.html' , {'error': 'Такой пользователь уже есть'} )
        else:
            return render ( request , 'linker/main_page.html' , {'error': 'Пароли должны совпадать'} )


def login_user (request):
    
    if request.method == 'GET':
        
        if request.user.is_authenticated:
            return redirect ('home')
        else:
            return render ( request , 'linker/main_page.html' )


    if request.method == 'POST':
        user = authenticate ( request , username = request.POST ["username"] , password = request.POST ["password"] )

        if user is None:
            return render ( request , 'linker/main_page.html' , {'user': user , 'error': 'Некорректный Логин/Пароль'} )

        else:
            login (request , user)
            return redirect ('home')


def logout_user (request):

    if request.method == 'GET':
        logout (request)
        return redirect ('home')





        
        
    