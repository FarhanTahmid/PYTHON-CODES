#if statement
if 3>2:
    print("Its true!")

hungry=False
if hungry:
    print("feed me!")
else:
    print('not hungry')
print('\n')
x=int(input("Please enter X: "))
if x==5:
    print("The given input is 5")
else:
    print("The given input is not 5")

print("\n")
location=str(input("Enter the location: "))
if location == 'bank':
    print("Going to cashout money.")
elif location == 'Auto shop':
    print("Going to pick up my new car.")
elif location=='store':
    print("Going to pick up some grocery")
else:
    print("Unknown Location!")

#ternary operator:
print("\nTernary operator: ")
print("bank" if location== 'bank' else "unknown location!")