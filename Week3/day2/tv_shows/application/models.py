from django.db import models


class UserManager(models.Manager):

    def registrationValidator(self, postData):
        errors = {}
        if postData["first_name"] < 2:
            errors["first_name"] = "Name must be at least 2 character"

        if User.objects.filter(email = postData["email"]):
            errors["email"] = "Account already exists, please log in"

        return errors

    def loginValidator(self, postData):
        if not User.objects.filter(email = postData["email"]):
            errors["email"] = "Account not found"
        else:
            
            if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
                errors["password"] = "Login failed"
            else:
                print("failed password")

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
    