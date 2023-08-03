from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('admins/', admins, name='admins'),
    path('logout/', logout , name='logout'),
    path('subject/', subject , name='subject'),
    path('cycles/', cycles, name = 'cycles'),
    path('editar_cycle/<int:ciclo_id>/', editar_cycle, name='editar_cycle'),
    path('eliminar_cycle/<int:ciclo_id>/', eliminar_cycle, name = 'eliminar_cycle')
]