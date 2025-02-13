from django.contrib import admin
from .models import Task, DailyTask, WeekTask, MonthTask

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'type', 'created_at')  
    search_fields = ('title', 'description')  
    list_filter = ('completed', 'type')  

admin.site.register(Task, TaskAdmin)
admin.site.register(DailyTask)
admin.site.register(WeekTask)
admin.site.register(MonthTask)

