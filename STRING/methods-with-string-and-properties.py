a='z'
b='2'
c='3'
print(b+c)
print(a*10)
#concatanating a letter in a string
print("\nConcatanating a STRING")
name="sam"
last_two_letter= name[1:]
print(last_two_letter)
new_name='P'+ last_two_letter
print(new_name)

#uppercasing and lowercasing
print("\nUppercasing a letter")
print(name.upper())
print(name.lower())

#splitting string
print("\nSplitting string")
x="this is a string"
print(x.split()) #output shows as a list
print(x.split('i')) #i is removed from all the words

#.format string
print("\nUsing Format string - (.format)")
print("This is a string {}".format("INSERTED"))
print("The value of x inserted in the function was {}. and the value of name inserted was {}".format(x,name))
print("\nWith index declared string formatting")
print("The value of name inserted was {1} and The value of x inserted in the function was {0}.".format(x,name)) #index formatting

print("The {} {} {}".format("quick", "brown", "fox"))
print("The {2} {2} {2}".format("quick", "brown", "fox"))
print("The {1} {0} {2}".format("quick", "brown", "fox"))

#variable declared inside .format string
print("\nWith variable declared format string:\n{b} {q} {f}".format(q="quick", b="brown", f="fox"))

#f-string method
print("\n\t\tF-string method:\n")
myName="Farhan Ishrak Tahmid"
age=20
print(f"Hello! My name is {myName}")
print(f"{myName} is {age} years old.")