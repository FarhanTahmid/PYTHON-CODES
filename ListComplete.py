#initializing a string
print("Initializing a string")
list1=[1,2,3]
list2=["string",100,23.2]
print(list1)
print(list2)

#length of a list
print("\nLength of a list : ")
l=len(list2)
print(f"Length of list 2 is {l}")

#grabbing elements with index
print("\nGrabbing elements with index:")
print("The second element of list 2 is: {}".format(list2[1]))

#concatanate two list
print("\nConcatanating two list:")
print("Concatanating first and second list:\n{}".format(list1+list2))

#mutatitng list
print("\nMutating List 2:")
list2[0]="Men and Women"
print(list2)

#appending list
print("Appending List:")
list2.append("Six")
print(list2)

#removing item from list
print("\nRemoving item from list:")
list1.pop()
print(list1)
print("Removing item from specific index")
list2.pop(2)
print(list2)

#sort a list in order
print("\nSorting a list in order: ")
list3=['a','e','b','x','j','k']
list4=['4','2','6','1','9']
list3.sort() 
#sortedlist3=list3 (if you want to assign another variable name)
print(list3) #or, print(sortedlist3)
list4.sort()
print(list4)

#reversing a list
print("\nReversing a list: ")
list4.reverse()
print(list4)




