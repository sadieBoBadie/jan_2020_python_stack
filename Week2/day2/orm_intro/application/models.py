from django.db import models


# Create your models here.
class User(models.Model):
    # id --> primary key
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects ==> Manager

    def __repr__(self):
        return f"User: {self.first_name} {self.last_name}"

