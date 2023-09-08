from django.db import models
from datetime import datetime
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank=True)
    finished = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def  __str__(self):
        return self.title