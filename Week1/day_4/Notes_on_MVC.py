# [ ] MVC / Model  Template  Views

# Fat Models/ Skinny Controllers

#        (Django)                        (Django)
# View/Templates             Controller/Views.py  // flask -> server.py                      

# Browser                    - Logic
# What client sees           Receives incoming requests
                            # Minimal logic
                            # Calls on models to aggregate/process data
                            # Determines appropriate response
# Front-End


# Models  ---> Object  Relational  Mapping
# -- interfaces with DB
# May build database tables
# Handles logic that relies on data
# Interfaces with the database

# CLASSES

class User:
    def __init__(self):
        self.first_name
        self.last_name
        self.email
        self.password









# [ ] Modularization / Folder Structure

# [ ] Set up and making a CHEAT SHEET
# 		—encountering errors yourself is important!


#  BROWSER --> url -> http request --> SERVER --> settings --> 
#               project urls --> app urls --> views.py ---> return HTTP RESPONSE