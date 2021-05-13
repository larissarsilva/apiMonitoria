from .models import Napsi, Professor, Aluno, Disciplina
from .serializers import NapsiSerializer, ProfessorSerializer, AlunoSerializer, DisciplinaSerializer

from rest_framework import generics 

# Listar e Criar
class NapsiList(generics.ListCreateAPIView):
    queryset = Napsi.objects.all()
    serializer_class = NapsiSerializer

#Editar, Detalhes e Excluir
class NapsiRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Napsi.objects.all()
    serializer_class = NapsiSerializer

# Listar e Criar Professor
class ProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

#Editar, Detalhes e Excluir Professor
class ProfessorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

# Listar e Criar Aluno
class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

#Editar, Detalhes e Excluir Aluno
class AlunoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer    


# Listar e Criar Disciplina
class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

#Editar, Detalhes e Excluir Disciplina
class DisciplinaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer      