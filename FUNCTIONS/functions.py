#initializing a function
print("\nInitializing a function\n")
def function1():
    print("hello")
function1()

#function with parameters
print("\nFunction with parameters: ")
def add_func(num1,num2):
    print(f"Addition result: {num1+num2}")
add_func(5,7)

#returning a value
print("\nReturning a value")
def substraction(num1,num2):
    return(num1-num2)
result=substraction(1122,889)
print(f"Substraction Value is {result}")

#PIG LATIN
print("\nPig Latin Method")
def pig_latin(word):
    first_letter=word[0]
    if first_letter in 'aeiou':
        new_word= word +'ay'
    else:
        new_word= word[1:]+first_letter+'ay'
    return new_word
vowel_check= input("Please enter a word to check if the first letter is vowel: ")
result=pig_latin(vowel_check)
print(f"Result: {result}")

def pig_latin(word):
    first_letter=word[0]
    if first_letter== 'a' or 'e' or 'i' or 'o' or 'u':
        new_word= word +'ay'
    else:
        new_word= word[1:]+first_letter+'ay'
    return new_word
vowel_check= input("Please enter a word to check if the first letter is vowel: ")
result=pig_latin(vowel_check)
print(f"Result: {result}")

'''
function will return smaller number if two numbers are even and if its odd then it will return the smallest between two numbers
'''