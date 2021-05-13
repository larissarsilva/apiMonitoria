from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField

#models.ForeignKey('users.User', on_delete = models.PROTECT)
class Napsi(AbstractUser):
    nome = models.CharField(max_length=40)
    email = models.EmailField(unique=True)

class Professor(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=14)
    cpf = models.CharField(max_length=11)

class Aluno(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    periodo = models.IntegerField()
    curso = models.CharField(max_length=40)
    turno = models.CharField(max_length= 7)
    historico = models.CharField(max_length=250)
    
  
class Disciplina(models.Model):
    codigo = models.CharField(max_length=12) 
    nome = models.CharField(max_length=40) 
    professor = models.ForeignKey('users.Professor',on_delete=models.PROTECT)

class Candidato(models.Model):
    aluno = models.ForeignKey('users.Aluno', on_delete = models.PROTECT)
    disciplina = models.ForeignKey('users.Disciplina', on_delete = models.PROTECT)
    # Candidato Aprovado

'''
class Monitor(models.Model):
    candidatura = models.ForeignKey('users.Candidato', on_delete = models.PROTECT)

class Monitoria(models.Model):
    professor = models.ForeignKey('users.Aluno', on_delete = models.PROTECT)
    monitor = models.ForeignKey('users.Aluno', on_delete = models.PROTECT)
    disciplina = models.ForeignKey('users.Aluno', on_delete = models.PROTECT)

'''

