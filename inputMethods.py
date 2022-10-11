
#Taking input without typecasting
print("\nTaking input without typecasting:")
a=input("Please input anything here: ")
b=input("Please input something here: ")
c=input("Please input a number here: ")

#type of input taken
print("\nType of inputs:")
print(f"Type of input value:{type(a)}")
print(f"Type of input value:{type(b)}")
print(f"Type of input value:{type(c)}")

#adding the values
print("\nAdding the values: ")
d=a+b+c
print(f"Added value is {d}")
print("We can see that all these are adding up as string. So to get specific inputs we need typecasting")

#typecasting input
print("\nTypecasting input: ")
num1=int(input("Please Enter an integer number here: "))
num2=int(input("Please enter another integer number here: "))
num3=int (input("Please enter another number here: "))
value_added= num1+num2+num3
print(f"The added value is {value_added}")

#type of inputs
print(f"Now we can see the type of inputs as {type(num1)}, {type(num2)}, {type(num3)}")

#string input
print("\nstring input")
string1=str(input("Please enter a string here: "))
print(f"The type of the input is: {type(string1)}")
print(f"Inputted string: {string1}")

#float input
print("\nFloat input: ")
float1=float(input("Please enter a broken value: "))
print(f"Entered value: {float1}")
print(f"Type of the input: {type(float1)}")
 
