from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):#cria o serializador 
    class Meta:
        model = Task #o modelo dos campos que serao convertidos
        fields = '__all__' #todos os campos serao convertidos para JSON