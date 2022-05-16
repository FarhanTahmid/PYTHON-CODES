import arbitaryNumberOfArguments

arbitaryNumberOfArguments.makePizza(16,'mushroom sauce','pepperoni','extra cheese') #this type of importing includes all the line of code written in the imported file

from arbitaryNumberOfArguments import makePizza,buildProfileOfUser
makePizza(16,'mushroom sauce','pepperoni','extra blue cheese') #this only imports the function you want to import

#another type of import is:
from arbitaryNumberOfArguments import makePizza as mojarPizza
mojarPizza(12,'mushroom sauce','pepperoni','extra kalabhuna')

#importing all the functions in a module
from arbitaryNumberOfArguments import *
makePizza(13,"Kimchi chicken")
print("Using the function named build profile of user")
user=buildProfileOfUser("zaed",'khan',
                   location='dhanmondi',university='nsu'
                   )
print(user)