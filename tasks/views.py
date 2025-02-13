from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, get_object_or_404
from copy import deepcopy
from .models import Task, TimeTask

@api_view(['GET'])  #decorador que faz com que a task_list vai executar "GETS"
def task_list(request):
    tasks = Task.objects.all()  # pega as tasks que passamos
    serializer = TaskSerializer(tasks, many=True)  # converte as tasks para JSON
    return Response(serializer.data)  # volta os dados como JSON

@api_view(['delete'])
def rem_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
    except Task.DoesNotExist:
        return Response({"error": "Tarefa não encontrada!"}, status=404)
    
@api_view(['GET'])
def search_task(request, task_title):
    try:
        task = Task.objects.get(title=task_title)
        serializer = TaskSerializer(task, many=True)  
        return Response(serializer.data) 
    except Task.DoesNotExist:
        return Response({"error": "Tarefa não encontrada!"}, status=404)

@api_view(['PUT', 'PATCH'])
def edit_task(request, task_id):
    new_task = get_object_or_404(Task, id=task_id)
    serializer = TaskSerializer(new_task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)
    

@api_view(['POST'])
def migrate_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    new_type = request.data.get("new_type")  # dia semana mes
    new_value = request.data.get("new_value")  # derivado dia semana mes 
    move_task = request.data.get("move", False)  # remove origin

    if not new_type or not new_value:
        return Response({"error": "Você deve fornecer um tipo (D, S, M) e um valor correspondente."}, status=400)

    if new_type not in dict(TimeTask.TIME_CHOICES):
        return Response({"error": "Tipo inválido. Use 'D' para dia, 'S' para semana ou 'M' para mês."}, status=400)

    time_task_data = {"time": new_type, "tarefa": task}

    if new_type == "D":  
        if new_value not in dict(TimeTask.DAILY_CHOICES):  
            return Response({"error": "Dia inválido."}, status=400)
        time_task_data["day"] = new_value

    elif new_type == "S":  
        if new_value not in dict(TimeTask.WEEK_CHOICE):  
            return Response({"error": "Semana inválida."}, status=400)
        time_task_data["week"] = new_value

    elif new_type == "M": 
        if new_value not in dict(TimeTask.MONTH_CHOICES):  
            return Response({"error": "Mês inválido."}, status=400)
        time_task_data["month"] = new_value

    time_task = TimeTask.objects.create(**time_task_data)

    if move_task:
        task.delete()

    return Response({"message": "Tarefa migrada com sucesso!"}, status=201)