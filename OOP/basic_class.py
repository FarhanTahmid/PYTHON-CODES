class Dog:
    attr1="mammal"
    attr2='dog'

    def fun(self):
        print(f"I am a {self.attr1}")
        print(f"This is a {self.attr2}")
    
rodger=Dog()
print(rodger.attr1)
rodger.fun()

