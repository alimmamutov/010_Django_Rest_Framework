from django.db import models
from service.settings import AUTH_USER_MODEL as User

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
