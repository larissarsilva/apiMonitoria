from rest_framework import serializers
from .models import Napsi, Professor, Aluno, Disciplina

class NapsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Napsi
        fields = ('id','first_name','last_name','username','email','password')

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'