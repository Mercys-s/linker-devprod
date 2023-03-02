from django.urls import path 

from .views import subject_category , subject_item 



urlpatterns = [
    path ('' , view = subject_category , name = 'subject_category'),
    path ('task/<slug:subject_item_slug>/' , view = subject_item , name = 'subject_item'),  
] 