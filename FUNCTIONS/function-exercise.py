'''
function will return smaller number if two numbers are even and if its odd then it will return the smallest between two numbers
'''
'''
def finalresult(a,b):
    if (a%2==0) and (b%2==0):
        if(a>b):
            print(f"{b} is the smallest one between ({a},{b}) numbers.")
        else:
            print(f"{a} is the smallest one between ({a},{b}) numbers.")
    elif (a%2!=0) and (b%2!=0):
        if(a>b):
            print(f"{a} is the greater one between ({a},{b}) numbers.")
        else:
            print(f"{b} is the greater one between ({a},{b}) numbers.")
    else:
        print("Both numbers are nor even nor odd.")

x =int(input("Enter the first number: "))
y =int(input("Enter the second number: "))
finalresult(x,y)
'''

'''
check if two words in a string starts with same letters
'''
'''
def checkwords(text):
    checker=text.split()
    if (checker[0][0]==checker[1][0]):
        print("true")
    else:
        print("false")
x=str(input("Enter a string which contains only two words: "))
checkwords(x)
'''

'''
return true if the sum of two integers are 20 or if one of the number is 20
'''
'''
print("return true if the sum of two integers are 20 or if one of the number is 20:\n")
def twenty(a,b):
    if (a+b==20) or a==20 or b==20:
        print("True")
    else:
        print("False")
        
x=int(input("Please enter the first number: "))
y=int(input("Please enter the second number: "))
twenty(x,y)
'''

'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
'''
'''
print("OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name:\n")

def capitalize(word):
    print(f"The returned word from thefunction is: {word[0].capitalize()+word[1:3]+word[3].capitalize()+word[4:]}")
z=str(input("Enter the word you want to capitalize: "))
capitalize(z)
'''

'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
'''

'''
print("MASTER YODA: Given a sentence, return a sentence with the words reversed: ")


def reveresed_string(string1):
    x=string1.split()
    z=" ".join(x[::-1])
    print(z)
y=str(input("Enter the string to reverse: "))
reveresed_string(y)
'''

'''
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
'''
'''
print("\nALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200\n")

def almost_there(x):
    if (100-x)<=10 or (x-100)>=10 or (x-200)>=10 or (100-x)<=10:
        return True
    else:
        return False

x=int(input("Please enter a number to test whether it is within 10 of 100 or 200: "))
print(almost_there(x))
'''

'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
'''
'''
print("Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.\n")

def find_3(list1):
    length=len(list1)
    for i in range(0,length-1):
        if list1[i]==3 and list1[i+1]==3:
            return True
    return False

n=int(input("How many elements do you want in the list: "))
list2=[]
for i in range(0,n):
    x=int(input(f"{i}:"))
    list2.append(x)
print(find_3(list2))
'''

'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
'''
'''
print("\nBLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'\n")

def blackjack(x,y,z):
    if (x+y+z)<=21:
        return x+y+z
    elif (x+y+z)>21 and (x==11 or y==11 or z==11):
        adjustment= (x+y+z)-10
        if adjustment>21:
            return 'BUST'
        elif adjustment<=21:
            return adjustment
print("Enter Three integers to check: ")
a=int(input())
b=int(input())
c=int(input())
print(blackjack(a,b,c))
'''

'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
'''
'''
print("\nPAPER DOLL: Given a string, return a string where for every character in the original there are three characters:")
def triplin_letters(string1):
    result=" "
    for char in string1:
        result+=char*3
    return result

str1=str(input("Enter the word:"))
print(triplin_letters(str1))
'''

'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
'''
'''
print("\nSUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.")

def sum_except(list):
    sum =0
    for x in range (0,len(list)):
        if list[x]!=6:
            sum+=list[x]
        elif list[x]==6:
            break;
        elif list[x]==9:
            break;
    return sum
n= int(input("\nEnter the number of elements you want in the list: "))

list1=[]
for i in range(0,n):
    y=int(input(f"{i}:"))
    list1.append(y)
print(sum_except(list1))
'''

'''
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
'''

print("\nSPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order")

def true_in_sequence(list):
    for x in range (0,len(list)):
        if (list[x:x+3]!=[0,0,7]):
            return False
            continue
        elif(list[x:x+3]!=[0,0,7]):
            return True
            break

n=int(input("Enter how many elements you want in the list: "))
list1=[]
for i in range(0,n):
    y=int(input(f"{i}:"))
    list1.append(y)
print(true_in_sequence(list1))



