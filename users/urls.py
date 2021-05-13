from django.urls import path
from users.endpoints import *

app_module = 'users'

urlpatterns = [
    path('napsi',NapsiList.as_view()),
    path('edit-user/<int:pk>', NapsiRetrieveUpdateDestroy.as_view()),

    path('professor/', ProfessorList.as_view()),
    path('edit-professor/<int:pk>', ProfessorRetrieveUpdateDestroy.as_view()),

    path('aluno/', AlunoList.as_view()),
    path('edit-aluno/<int:pk>', AlunoRetrieveUpdateDestroy.as_view()),

    path('disciplina/', DisciplinaList.as_view()),
    path('edit-disciplina/<int:pk>', DisciplinaRetrieveUpdateDestroy.as_view()),


]