from email.policy import default
from django.db import models

from accounts.models import User

# TODO model table
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'