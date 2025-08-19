from django.db import models
from abc import abstractmethod

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @abstractmethod
    def __str__(self):
        pass

class Post(BaseModel):
    
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title