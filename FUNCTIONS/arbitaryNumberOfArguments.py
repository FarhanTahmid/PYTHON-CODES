def makePizza(size,*toppings):
    print(f"Making {size} inch pizza with following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
makePizza(8,'pepperoni')
makePizza(16,'mushrooms','green peppers','extra cheese')

#Using arbitary keyword arguments
def buildProfileOfUser(firstName,lastName,**userInfo):
    userInfo['first_Name']=firstName
    userInfo['last_name']=lastName
    return userInfo
user_profile=buildProfileOfUser('farhan','tahmid',
                                location='dhaka',university='nsu'
                                )
print(user_profile)


