from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Feedback(models.Model):
    subject = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.subject[:20] + "__" + self.content[:30]
