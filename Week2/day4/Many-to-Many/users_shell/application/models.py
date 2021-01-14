from django.db import models

# Create your models here.
# Users can join many projects, and projects can have many users

class User(models.Model):
    # id
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # list of Project objects
    # projects

    def __repr__(self):
        return f"User: {self.id} {self.first_name} {self.last_name}"

class Project(models.Model):
    #id
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    description = models.TextField()
    # a list of user objects
    users = models.ManyToManyField(User, related_name="projects")