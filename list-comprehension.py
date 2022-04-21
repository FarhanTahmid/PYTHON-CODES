#Assigning a list with for loop
print("Assigning a list with a normal loop: ")
string1='farhan tahmid'
list1=[]
for letter in string1:
    list1.append(letter)
print(f"New created list: \n{list1}")

#list comprehension
print("\nList Comprehension: ")
list2=[letter for letter in string1]
print(f"After list comprehension: \n{list2}")

print("\nWithout declaring seperate string variable: ")
list3=[x for x in 'neha']
print(f"\nList 3 is: {list3}") 

print("\nList comprehension in range: ")
list4=[number for number in range(0,10)]
print(f"List 4 is; {list4}")

print("\nList comprehension with logic: ")
list5=[number for number in range(0,10) if number%2==0]
print(f"List 5 is: {list5}")
list5=[number**2 for number in range(0,10) if number%2==0]
print(f"Square form: {list5}")

#converting temperature
print("\nConvert temperature from celcius to fahrenheit:\n")
celcius_temp=[0,10,20,26,45,60]
print(f"Given celcius temperature: {celcius_temp}")
fahrenheit_temp=[(9/5*temp+32)for temp in celcius_temp]
print(f"Converted temperature from celcius to fahrenheit:\n{fahrenheit_temp}")

#if else in list comprehension:

print("\nIf else in list comprehension:")
result=[x if x%2==0 else "ODD" for x in range(0,10)]
print("The result is: {}".format(result))