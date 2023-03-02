from django.shortcuts import render


def main_page (request):
    return render (request , 'linker/main_page.html')