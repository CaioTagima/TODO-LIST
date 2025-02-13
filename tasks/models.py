from django.db import models
import datetime

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

    title = models.CharField(max_length=50,verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    completed = models.CharField(max_length=1, default='C', choices=STATUS_CHOICES,verbose_name='Andamento')
    type = models.CharField(max_length=1, default='L', choices=TASKTYPE_CHOICES,verbose_name='Tipo da Tarefa')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Horário de Criação')
    priority = models.CharField(max_length=1, default='M', choices=PRIORITY_CHOICES,verbose_name='Prioridade')
    task_time = models.TimeField(default=datetime.time(22, 0),verbose_name='Horario da Tarefa')

    def __str__(self):
        return self.title


class TimeTask(models.Model):
    TIME_CHOICES = [ 
        ('D', 'Dia'),
        ('S', 'Semana'),
        ('M', 'Mes'),
    ]

    DAILY_CHOICES = [ 
        ('SEG', 'Segunda'),
        ('TER', 'Terça'),
        ('QUA', 'Quarta'),
        ('QUI', 'Quinta'),
        ('SEX', 'Sexta'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]

    WEEK_CHOICE = [
        ('1', 'Primeira Semana'),
        ('2', 'Segunda Semana'),
        ('3', 'Terceira Semana'),
        ('4', 'Quarta Semana'),
    ]

    MONTH_CHOICES = [ 
        ('JAN', 'Janeiro'),
        ('FEV', 'Fevereiro'),
        ('MAR', 'Março'),
        ('ABR', 'Abril'),
        ('MAI', 'Maio'),
        ('JUN', 'Junho'),
    ]

    time = models.CharField(max_length=1, choices=TIME_CHOICES,verbose_name='Período')
    day = models.CharField(max_length=3, choices=DAILY_CHOICES, null=True, blank=True,verbose_name='Dia')
    week = models.CharField(max_length=1, choices=WEEK_CHOICE, null=True, blank=True,verbose_name='Semana')
    month = models.CharField(max_length=3, choices=MONTH_CHOICES, null=True, blank=True,verbose_name='Mês')
    tarefa = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        if self.time == 'D' and self.day:
            return f"{self.tarefa.title} - {self.day}"
        elif self.time == 'S' and self.week:
            return f"{self.tarefa.title} - Semana {self.week}"
        elif self.time == 'M' and self.month:
            return f"{self.tarefa.title} - {self.month}"
        return f"{self.tarefa.title} - Sem data definida"
