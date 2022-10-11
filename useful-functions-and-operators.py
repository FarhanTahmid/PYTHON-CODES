#range function
print("\nUse of range function: ")
print("With random values: ")
for num in range(5):
    print(num)
print("With start and stop point:")
for num in range(2,10):
    print(num)
print("With start, stop and step number")
for num in range(2,20,3):
    print(num)

#creating a list with random function
print("\nCreating a list with random function:")
list1=list(range(2,20,3))
print(list1)

#enumerate function
print("\nCounting the index number of letters in a string with normal for loop: ")
index_count=0;
for letter in 'farhan':
    print(f"The letter {letter} is at {index_count} index.")
    index_count+=1

#same counting with enumerate function:
print("\nSame counting with enumerate function:")
name="farhan"
for item in enumerate(name):
    print(item)
print("\nAnother method with enumerate function: ")
for index,letter in enumerate(name):
    print(index)
    print(letter)
    print("\n")

print("Only printing the indexes:")
for index,item in enumerate(name):
    print(index)


#ZIP FUNCTION
print("\nZip function: ")
list2=[1,2,3]
list3=['a','b','c']
for item in zip(list2,list3):
    print(item)

print("\nAnother one: ")
list4=['father','mother','son']
for item in zip(list2,list3,list4):
    print(item)

print("\nRminder:\nZip function is gonna work with the least amount of value stored in a list. so uneven lsits cant be zipped with this function:")
print("Getting output as list with zip function")
list5=list(zip(list2,list3,list4))
print(list5)

#in operator
print("\nIn operator:")
x='father'in list4
print(x)
y= 1 in list3
print(y)
dict1={'k':132,3:'kyj'}
checker1= 'k' in dict1
print(checker1)
checker2= 132 in dict1.values()
print(checker2)

#library import
print("\nLibrary import:")
print("\nShuffling a list: ")
from random import shuffle
list6= [1,2,3,4,5,6,7,8,9,0]
print(f"Before shuffle the list was: {list6}")
x=shuffle(list6)
print(f"After shuffling: {list6}")
print(type(x))

#importing random number:
print("\nImporting random number: ")
from random import randint
random1=randint(0,100)
print(f"The random number is {random1}")


