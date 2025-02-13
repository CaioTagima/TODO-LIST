from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('C', 'Criado'),
        ('E', 'Em andamento'),
        ('F', 'Finalizado'),
    ]

    TASKTYPE_CHOICES = [
        ('L', 'Lembrete'),
        ('E', 'Evento'),
        ('N', 'Nota'),
        ('M', 'Meta'),
    ]

    PRIORITY_CHOICES = [ 
        ('A', 'Alta'),
        ('M', 'Média'),
        ('B', 'Baixa')
    ]

    title = models.CharField(max_length=50)#titulo da task
    description = models.TextField()
    completed = models.CharField(max_length=1,default='C',choices= STATUS_CHOICES)#andamento da task
    type = models.CharField(max_length=1,default='L',choices=TASKTYPE_CHOICES)#tipo da task 
    created_at = models.DateTimeField(auto_now_add=True) #data de criação da task
    priority = models.CharField(max_length=1,default='M',choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title #quando listarmos o objeto sera o title
    
class MonthTask(models.Model):
    MONTH_CHOICES = [ 
        ('JAN', 'Janeiro'),
        ('FEV', 'Fevereiro'),
        ('MAR', 'Março'),
        ('ABR', 'Abril'),
        ('MAI', 'Maio'),
        ('JUN', 'Junho'),
    ]
    month = models.CharField(max_length=3,choices=MONTH_CHOICES)
    tarefa = models.ForeignKey(Task,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.tarefa.title} - {self.month}" if self.tarefa else f"Sem tarefa - {self.month}"

class WeekTask(models.Model):
    WEEK_CHOICE = [
        ('1', 'Primeira Semana'),
        ('2', 'Segunda Semana'),
        ('3', 'Terceira Semana'),
        ('4', 'Quarta Semana'),
    ]
    week = models.CharField(max_length=1,choices=WEEK_CHOICE, null=True, blank=True)
    mes = models.ForeignKey(MonthTask,on_delete=models.CASCADE, null=True, blank=True)
    tarefa = models.ForeignKey(Task,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.tarefa.title} - {self.week}" if self.tarefa else f"Sem tarefa - {self.week}"

class DailyTask(models.Model):
    DAILY_CHOICES = [ 
        ('SEG', 'Segunda'),
        ('TER', 'Terça'),
        ('QUA', 'Quarta'),
        ('QUI', 'Quinta'),
        ('SEX', 'Sexta'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]
    day = models.CharField(max_length=3,choices=DAILY_CHOICES)
    tarefa = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    semana = models.ForeignKey(WeekTask,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.tarefa.title} - {self.day}" if self.tarefa else f"Sem tarefa - {self.day}"






