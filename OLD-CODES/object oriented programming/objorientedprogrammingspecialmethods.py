class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

b= Book("Python rocks","Farhan","200")
print(b)
#OUTPUT: <__main__.Book object at 0*x0000015B.... (actually shows where its saved in memory)\
str(b)
#OUTPUT: <__main__.Book object at 0*x0000015B.... (actually shows where its saved (as string) in memory)\


#FOR STRING CALL

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

b= Book("Python rocks","Farhan","200")
print(b)
#OUTPUT: 'Python rocks by Jose'
str(b)
#OUTPUT: 'Python rocks by Jose'


#CHECKING LENGTH

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

b= Book("Python rocks","Farhan","200")
print(b)
#OUTPUT: 'Python rocks by Jose'
str(b)
#OUTPUT: 'Python rocks by Jose'
len(b)
#OUTPUT: 200



#Deleting variables

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

b= Book("Python rocks","Farhan","200")
print(b)
#OUTPUT: 'Python rocks by Jose'
str(b)
#OUTPUT: 'Python rocks by Jose'
len(b)
#OUTPUT: 200
del (b)
b
#OUTPUT: Name error


#FOR PRINTING OUT A DELETED TEXT

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print (A object has been deleted)

b= Book("Python rocks","Farhan","200")

print(b)
#OUTPUT: 'Python rocks by Jose'
str(b)
#OUTPUT: 'Python rocks by Jose'
len(b)
#OUTPUT: 200
del (b)
#OUTPUT: A book object has been deleted
