from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    # Note! This code is incomplete, you will need to
    # ensure that all cases are taken care of.

    def registrationValidator(self, postData):
        errors = {}
        # first and last blank?
        if len(postData["first_name"]) == 0:
            errors["first_name_blank"] = "First required."
        elif len(postData["first_name"]) < 2:
            errors["first_name"] = "First needs at least 2 characters"

        if len(postData["last_name"]) < 2:
            errors["first_name"] = "First needs at least 2 characters"
        
        # email blank

        # Email right format? --> regex
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        
        # Password: 
        #   length > 8, optional pattern validation,
        #   check if pw and confirm are the same
        if postData["password"] != postData["confirm_password"]:
            errors['password'] = "Passwords do not match!"

        # in views??
        # Check if already in DB
        user = User.objects.filter(email=postData["email"])
        if user:
            errors['email'] = "Account already exists."
        # if is an empty list -- good to go
        # if not empty error
        print("*"*30)
        print(test)

        return errors
    

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    pw_hash = models.CharField(max_length=255)

    objects = UserManager()

class ShowManager(models.Manager):
    
    def basic_validator(self, postData):
         # create a dictionary of messages 
        errors = {}

        if len(postData["title"]) == 0:
                errors["title"] = "Title must not be blank."

        if len(postData["network"]) == 0:
            errors["network"] = "Network must not be blank."

        if len(postData["description"]) == 0:
            errors["description"] = "Description must not be blank."

        if len(postData["release_date"]) == 0:
            errors["release_date"] = "Release date required."

        return errors
        



class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    def __repr__(self):
        return f"Show: {self.title} {self.network}"
    