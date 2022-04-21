#creating a class
class Myclass:
    x=5
#creating an object with the use of that class:
p1=Myclass()
print(p1.x)

class Dog:
    def __init__(self,name,age):   #self is used for differentiating...like ekek shomoy ekekta dog er jonno jodi amra class ta ke call korte chai then amra parameter e name pass korle self sheta indicate kore dey je amra kon dog niye kaj kortesi

        self.name=name
        self.age=age

    
    def getname(self):
        return self.name
    
    def add_one(self,x):
        return x+1

    def bark(self):
        print("bark")
    
    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age=age

d=Dog(name="Batman",age=10) #here  we are instantiating, creating a new instance of a class dog, d is now and object of type dog
d2=Dog("Superman",8)

print("\nTesting the type of d:")
print(type(d))
print("\nNow we are gonna call the bark function as a method inside the class dog: ")
d.bark()
print("\nUsing method for the add_one function: ")
print(d.add_one(5))

print("\nGetting dog names:")
print(d.getname())
print(d2.getname())

print("\nGetting dog age")
print(d.get_age())
print(d2.get_age())

print("Now changing the age value with another method inside the class:")
d.set_age(30)
d2.set_age(12)
print("Now the set age function is called with self variable its gonna change the age from the whole class. So if we want to print the age from get age method we will see the changed result:")
print(d.get_age())
print(d2.get_age())

print("\nprinting different things for different dogs: ")
print(f"First dog's name was {d.getname()} and his age is {d.get_age()}")
