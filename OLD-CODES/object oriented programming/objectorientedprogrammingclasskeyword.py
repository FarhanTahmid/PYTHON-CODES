class Dog():
    def __init__(self,breed):
        self.breed = breed
my_dog = Dog(breed='Lab')
type(my_dog)
#output: __main__.Dog
my_dog.breed
#output: 'Lab'




class Dog():
    def __init__(self,mybreed):
        #attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = mybreed
my_dog = Dog(mybreed='Huskie')
type(my_dog)
#output: __main__.Dog
my_dog.breed
#output: 'Huskie'



class Dog():
    def __init__(self,mybreed,name,spots):
        #attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = mybreed
        self.name = name
        self.spots = spots
my_dog = Dog(breed='Huskie',name='Sammy',spots=False)
type(my_dog)
#output: __main__.Dog
my_dog.breed
#output: 'Lab'
my_dog.name
#output: 'Sammy'
my_dog.spots
#output: False




class Dog():
    #class object attributes
    #same for any instance of class
    species = 'mammal'
    def __init__(self,mybreed,name,spots):
        #attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = mybreed
        self.name = name
        self.spots = spots
my_dog = Dog(breed='Lab',name='Sammy',spots=False) #no need to define species here
type(my_dog)
#output: __main__.Dog
my_dog.breed
#output: 'Lab'
my_dog.name
#output: 'Sammy'
my_dog.spots
#output: False
my_dog.species
#output: 'mammal'




class Dog():
    #class object attributes
    #same for any instance of class
    species = 'mammal'
    def __init__(self,mybreed,name):
        #attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = mybreed
        self.name = name

    #OPERATIONS/ ACTIONS ----> METHODS
    def bark(self):
        print('Woof!')
my_dog = Dog('Lab','Sammy')
type(my_dog)
#output: __main__.Dog
my_dog.breed
#output: 'Lab'
my_dog.name
#output: 'Sammy'
my_dog.spots
#output: False
my_dog.species
#output: 'mammal'
my_dog.bark()
#output: Woof!



#adding dog name with bark
class Dog():
    #class object attributes
    #same for any instance of class
    species = 'mammal'
    def __init__(self,mybreed,name):
        #attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = mybreed
        self.name = name

    #OPERATIONS/ ACTIONS ----> METHODS
    def bark(self):
        print("Woof!My name is {}".format(self.name))#shudhu name dile hobe na...self.name lagbe cause oitai redirect korbe
my_dog = Dog('Lab','Sammy')
type(my_dog)
#output: __main__.Dog
my_dog.breed
#output: 'Lab'
my_dog.name
#output: 'Sammy'
my_dog.spots
#output: False
my_dog.species
#output: 'mammal'
my_dog.bark()
#output: Woof! My name is frankie



#added argument
class Dog():
    #class object attributes
    #same for any instance of class
    species = 'mammal'
    def __init__(self,mybreed,name):
        #attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = mybreed
        self.name = name

    #OPERATIONS/ ACTIONS ----> METHODS
    def bark(self,number):
        print("Woof!My name is {}and the number is {}.".format(self.name,number))#shudhu name dile hobe na...self.name lagbe cause oitai redirect korbe
my_dog = Dog('Lab','Sammy')
type(my_dog)
#output: __main__.Dog
my_dog.breed
#output: 'Lab'
my_dog.name
#output: 'Sammy'
my_dog.spots
#output: False
my_dog.species
#output: 'mammal'
my_dog.bark(10)
#output: Woof! My name is frankie and the number is 10.



#new type of class
class Circle():
    #class object attribute
    pi = 3.14

    def __init__(self,radius=1): #here radius=1 means 1 is radius's DEFAULT value

        self.radius = radius
            #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
my_circle = Circle()
my_circle.pi
#output: 3.14
my_circle.radius
#output;1 (cause its a default value given)


#changing the default value
class Circle():
    #class object attribute
    pi = 3.14

    def __init__(self,radius=1): #here radius=1 means 1 is radius's DEFAULT value

        self.radius = radius
            #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
my_circle = Circle(30)  #changing the DEFAULT value of radius
my_circle.pi
#output: 3.14
my_circle.radius
#output: 30 (cause its changed now)
my_circle.get_circumference()
#output: 188.4



#creating a attribute without announciang a parameter
class Circle():
    #class object attribute
    pi = 3.14 #this one is the class obj attribute

    def __init__(self,radius=1): #here radius=1 means 1 is radius's DEFAULT value

        self.radius = radius
        self.area = radius*radius*self.pi
            #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
my_circle = Circle(30)  #changing the DEFAULT value of radius
my_circle.pi
#output: 3.14
my_circle.radius
#output: 30 (cause its changed now)
my_circle.get_circumference()
#output: 188.4
my_circle.area
#output : 2862.0
