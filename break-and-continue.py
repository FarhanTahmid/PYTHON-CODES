#BREAK STATEMENT
print("BREAK STATEMENT:\n")
fruits=['apple','banana','cherry']
for x in fruits:
    print(x)
    if x=='banana':
        break

#BREAK STATEMENT BUT THE PRINT FUNCTION APPEARS AFTER THE PRINT FUNCTION
print("\nBREAK STATEMENT BUT THE PRINT FUNCTION APPEARS AFTER THE PRINT FUNCTION")
fruits=['apple','banana','cherry']
for x in fruits:
    if x=='banana':
        break
    print(x)

#CONTINUE STATEMENT
print("\nCONTINUE STATEMENT:")
fruits=['apple','banana','cherry']
for x in fruits:
    if x=='banana':
        continue
    print(x)
