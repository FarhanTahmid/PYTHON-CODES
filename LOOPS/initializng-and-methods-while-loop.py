#initializing while loop
print("\nInitializing while loops: ")
#x=int(input("\nEnter the value of X: "))
x=0
while x<5:
    print(f"The current value of x is {x}")
    x+=1
else:
    print("X is not less -than 5")

#use of pass
print("\nUse of pass: ")
list1=[1,2,3,4,5]
for item in list1:
    pass
print("\nSee in the code (line 15). There is no statement for the FOR loop but this line(out of the loop block) is still being printed.\nBecause we used PASS to do so.")

#use of continue
print("\nUse of continue: ")
name="Farhan"
for letter in name:
    print(letter)
print("\nNow if i dont want to print a specific letter we can use the CONTINUE method:")
print("Not wanting to print 'a' here.")
for letter in name:
    if letter=='a':
        continue
    print(letter)

#break method
print("\nBreak method: ")
x=0
while x<10:
    if x==2:
        break
    print(x)
    x+=1