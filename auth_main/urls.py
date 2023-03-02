from django.urls import path
from .views import signup_user , login_user , logout_user




urlpatterns = [
    
    path ( '' , view = signup_user , name = 'signup' ),
    path ( 'login/' , view = login_user , name = 'login' ),
    path ( 'logout/' , view = logout_user , name = 'logout' ),

] 