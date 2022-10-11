class Animal():
    def __init__(self):
        print("ANIMAL CREATED")(self)


        def who_am_i(self):
            print("I am an animal")

        def eat(self):
            print("I am eating")
myanimal.eat()
#output: I am eating
myanimal.who_am_i()
#output: I am an animal


#now inheriting the base class
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")(self)


        def who_am_i(self):
            print("I am an animal")

        def eat(self):
            print("I am eating")

class Dog(Animal):   #this one is the derived class

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

myanimal.eat()
#output: I am eating
myanimal.who_am_i()
#output: I am an animal
mydog = Dog()
#output: Animal CREATED
        #Dog created.




#overwriting the derived class
#now inheriting the base class
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")(self)


        def who_am_i(self):
            print("I am an animal")

        def eat(self):
            print("I am eating")

class Dog(Animal):   #this one is the derived class

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    dfe who_am_i(self):
    print("I am a dog")

myanimal.eat()
#output: I am eating
myanimal.who_am_i()
#output: I am an animal
mydog = Dog()
#output: Animal CREATED
        #Dog created.
mydog.who_am_i()
#output: i am a dog
