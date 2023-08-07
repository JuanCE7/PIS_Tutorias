from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('admins/', admins, name='admins'),
    path('logout/', logout , name='logout'),
    path('tutoring/', tutoring , name='tutoring'),
    path('tutorias/<int:tutor_id>/', tutorias_tutor, name='tutorias_tutor'),
    path('cycles/', cycles, name = 'cycles'),
    path('editar_cycle/<int:ciclo_id>/', editar_cycle, name='editar_cycle'),
    path('eliminar_cycle/<int:ciclo_id>/', eliminar_cycle, name = 'eliminar_cycle'),
    path('subject/', subject , name='subject'),
    path('materia_delete/<int:subject_id>/', materia_delete, name = 'materia_delete'),
    path('materia_update/<int:subject_id>/', materia_update, name = 'materia_update'),
    #path('editSubject/', editarCurso),
    #path('deleteSubject/<codigo>', eliminarCurso)
]