from django.db import models

class Media(models.Model) :
    id = models.BigAutoField(primary_key=True)
    title = models.fields.CharField(max_length=75)
    available = models.fields.BooleanField(default=True)
    details = models.fields.TextField(max_length=300)