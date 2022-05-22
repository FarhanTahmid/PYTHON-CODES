class Dog:
    """Making a model dog"""
    def __init__(self,dogName,dogAge):
        self.dogName=dogName
        self.dogAge=dogAge
    def sit(self):
        print(f"The dog named {self.dogName} is sitting now and his age is {self.dogAge}")
    def rollOver(self):
        print(f"The dog named {self.dogName} just rolled over and his age is {self.dogAge}")

#Creating an instance of a class
myDog=Dog("Zaed",5)
#Accessing elements
print(f"My dog's name is {myDog.dogName} and his age is {myDog.dogAge}")
myDog.sit()
myDog.rollOver()