a='hello'
print(a)
b=len(a)
print(b)

##indexing
mystring="Hello World"
print(mystring[0])
print(mystring[-2]) #reverse indexing
print(mystring[-1])

##slicsing
mystring2="abcdefghijkl"
print(mystring2[2:])  ##from index 2 to last

print(mystring2[:3])  ##from the very beginning and upto index 3(means 0 to 2 cz its upto 3)

print(mystring2[3:6]) #from index 3 to 6

print(mystring2[::2]) #jumps to position from beginning to end(:: means beginning to an end)

print(mystring2[1:7:2]) #from 1 to 7 and jumps 2 position

print(mystring2[::-1]) #reverses the string

