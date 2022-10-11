#for loop
from typing import OrderedDict


print("\nInitializing for loop:\n")
list1=[1,2,3,4,5,6,7,8,9,10]
for num in list1:  #num variable can be whatever i want
    print(num)
#using another term instead of num
print("\nUsing another variable term instead of num: ")
for jelly in list1:
    print(jelly)

#printing something else instead of the numbers in set
print("\nPrinting something else instead of the numbers in set:")
for num in list1:
    print("Farhan is the best xD")

#logical
print("\nLogical: ")
for num in list1:
    if num%2==0:
        print(f"{num} : Even number")
    else:
        print(f"{num} : Odd number")

#sum of the list
print("\nSum of the list :")
sum=0
for num in list1:
    sum+=num
print(f"Sum of the elements inside the list is {sum}")

#iterating through a string
print("\nIterating through a string: ")
string1="Hello world"
i=0
for letter in string1:
    print(letter)
    i=i+1
print(f"Number of letters in the string: {i}")

#tuple unpacking
print("\nTuple unpacking method with for loop: ")
list2=[(1,2),(3,4),(5,6),(7,8)]
for tup in list2:
    print(tup)
print("After unpacking the list now unpacking the tuple: ")
for a,b in list2:
    #enter whatever number you want to print
    print(a)
    print(b)

#iterating through dictionary
print("\nIterating through dictionary")
print("\nYou will get only keys by this method: ")

dict1={'k1':1, 'k2':2,'k3':3}
for keys in dict1:
    print(keys)

print("\nMethod for printing all the items: ")
for items in dict1.items():
    print(items)

print("\nMethod for printing keys and values separately: ")
for key,value in dict1.items():
    print(key)
    print(value)
print("\n")
for key,value in dict1.items():
    print(f"{key} - {value}")

print("\nAnother method\n: ")
print("\nValues:")
for value in dict1.values():
    print(value)

print("\nKeys: ")
for keys in dict1.keys():
    print(keys)


#RANGE FUNCTION
print("*THE RANGE FUNCTION INCREMENTS BY 1 AUTOMATICALLY AND BY DEFAULT:")
print("RANGE FUNCTION:")
for x in range(6):
    print(x)

print("\nRange function with initial value:")
for x in range (2,6):
    print(x)
 
print("\nRange function with incrementing value. (the default is 1)")
for x in range (2,10,2):
    print(x)

#ELSE IN FOR LOOP
print("\nELSE IN FOR LOOP:")
for x in range(0,5):
    print(x)
else:
    print("The loop finished.")


#NESTED LOOPS
print("\nNESTED LOOPS:")
adj=["red","big","tasty"]
fruits=['apple','banana','water-melon']
for x in adj:
    for y in fruits:
        print(x,y)


#PASS STATEMENT
#for loops cant go empty but if you want to pass on a loop use pass statement
print("\nPASS STATEMENT:")
for x in range (6):
    pass
