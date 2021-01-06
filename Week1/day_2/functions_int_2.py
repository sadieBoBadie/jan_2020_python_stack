 
students = [
                        #0
        
     {'first_name':  'Michael', 'last_name' : 'Jordan'},

                        #1

     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
x = [ [5,2,3], [10,8,9] ]
z = [ {'x': 10, 'y': 20} ]

#      0  1  2  3
arr = [3, 4, 5, 6]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# [10,8,9]
x[1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
# {'first_name':  'Michael', 'last_name' : 'Jordan'}


# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30
z[0]['y'] = 30

#dictionaries: key/value pairs
players = sports_directory['soccer'] # ==> ['Messi', 'Ronaldo', 'Rooney']
players[0] = "Andres"

# OR




print(sports_directory)





