from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    text = models.TextField()
    expires_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return self.text
