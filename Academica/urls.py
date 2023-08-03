from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('admins/', admins, name='admins'),
    path('logout/', logout , name='logout'),
    path('subject/', subject , name='subject'),


    #path('editSubject/<codigo>', edicionCurso),
    #path('editSubject/', editarCurso),
    #path('deleteSubject/<codigo>', eliminarCurso)

]