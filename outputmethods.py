result=100/777
print("The result was {}".format(result))
#float formatting
print("\nUsing float formatting: ")
print("The result was {r:1.3f}".format(r=result))
print("\nYou can write it this way too: ");
print("The result was {:1.3f}".format(result)) #not using any extra variable

#f-string float formatting
print("\nUsin f-string method:")
print(f"The result was {result}")
print(f"The result was {result:1.3f}")

#another way
print("\nC program style")
print("The value of result was %1.3f" %result)

#print two output statement without printing new line:
print("Print two output statement without printing new line:")
print("Farhan",end=" ")
print("is the best")    