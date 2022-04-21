#POLYMORPHISM

class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())
#output: niko says woof!
print(felix.speak())
#output: felix says meow!



#demonstrating POLYMORPHISM

class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())
#output: niko says woof!
print(felix.speak())
#output: felix says meow!
for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak())
##output: <class '__main__.Dog'>
#         <class 'str'>
#         <class '__main__.Cat>'
#         <class 'str'>

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
#OUTPUT: niko says woof

pet_speak(felix)
#OUTPUT: felix says meow


#ABSTRACT CLASSES
class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplentedError("Subclass must implement this abstract method")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"
fido = Dog("Fido")

isis = Cat("Isis")
print(fido.speak())
#OUTPUT: Fido says Woof

print(isis.speak())
#OUTPUT: isis says meow
