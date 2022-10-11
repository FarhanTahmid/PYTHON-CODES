###############scroll through the last to see the actual implemation



 #creating a program
def add(n1,n2,):
    print(n1+n2)
add(10,20)
#OUTPUT: 30
##if we wanta a input:
number = 10
number2 = input("please provide a number")
#wants input: and you give the input 20
 add(number1,number2)
 print("something haappend")
#output : This will be an error cause i wanted a number in the input but you entered a string there cause the input was taken as string!
#And the print statement is never going to execute cause the previous line had a type error


### CREATE A CODE TO UNDERSTAND HOW TO HANDLE THE ERROR###
try:
    #want to attempt this code
    #may have an ERROR
    result = 10 + 20
except:
    print("hey it looks you aren't adding correctly")
result
#OUTPUT: 30

#RUNNING THE ERROR:
try:
    #want to attempt this code
    #may have an ERROR
    result = 10 + '20' #THIS IS AN ERROR CODE BECAUSE I MADE THE NUMBER 20 A STRING
except:
    print("hey it looks you aren't adding correctly")
result
#OUTPUT: hey it looks you aren't adding correctly
#N.B: SEE THERE IS NO ERROR CAUSE  I ALREADY TOOK THE PRE CAUTIONS  BY USING THE TRY AND EXCEPT METHOD


#TRY, EXCEPT, ELSE STATEMENT :

try:
    #want to attempt this code
    #may have an ERROR
    result = 10 + '20' #THIS IS AN ERROR CODE BECAUSE I MADE THE NUMBER 20 A STRING
except:
    print("hey it looks you aren't adding correctly")
else:
    print("add went well")
    print (result)
#OUTPUT: add went well
#       20


########################################################
###TRY, EXCEPT, FINALLY METHOD ##THIS IS THE MAIN METHOD##

#THIS ONE IS A RIGHT CODE
try:
    f = open('testfile','w')
    f.write("write a test line")

except TypeError:
    print("there was a type error")

except OSError:                     #OS ERROR IS A TYPE OF ERROR FOR THIS CASE. THERE ARE MANY TYPES 0F ERRORS, YOU CAN FIND MORE ERRORS IN THE PDF
    print('hey you have an os ERROR')
finally:
    print("i always run")
#OUTPUT: I always RUN


#THIS ONE IS A WRONG code

try:
    f = open('testfile','r')  ##giving 'r' instead of 'w' cause 'r' is not needed to execute the code tp write. "r" is for reading while 'w' is for writing
    f.write("write a test line")

except TypeError:
    print("there was a type error")

except OSError:
    print('hey you have an OSError')
finally:
    print("i always run")
#OUTPUT: hey you have an OSError
#        I always RUN


#easy way to run this method:

try:
    f = open('testfile','r')

except TypeError:
    print("All other exceptions")
##removed the OSError block because its not necessary if u dont remember and dont want to specify
finally:
    print("i always run")

#OUTPUT: All other excepptions
#        I always RUN




###using this method for a function which asks for a input from a user

def ask_for_init():
    try:
        result = int(input("please provide a number:"))
    except:
        print("whoops! that is not a number")
    finally:
        print("end of try/ except/finally")
ask_for_init()
#program will want a input now
#input:20
#OUTPUT: Please provide a number : 20
#       end of try/ except/finally

######now doing an ERROR

def ask_for_init():
    try:
        result = int(input("please provide a number:"))
    except:
        print("whoops! that is not a number")
    finally:
        print("end of try/ except/finally")
ask_for_init()
#program will want a input now
#input: word
#OUTPUT: Please provide a number : word
#       whoops! that is not a number       [This code is wrong because i changed the input from int to string]
#       end of try/ except/finally


#handling this error using WHILE LOOP that keeps going over and over again until you give the correct input


def ask_for_init():
    while True:

        try:
            result = int(input("please provide a number:"))
        except:
            print("whoops! that is not a number")
            continue
        else:
            print("yes thank you")
            break        #{this 'break' statement breaks the loop of the enclosed "for" or "while" loop}
        finally:
            print("end of try/ except/finally")
            print("i will always run at the end")

ask_for_init()
#program will want a input now
#input: 20
#OUTPUT: yes thank you
#       Please provide a number : 20
#       end of try/ except/finally

#program will want a input now AGAIN cause the break statement hasn't executed yet
#input: word
#OUTPUT: Whoops that is not a number
#       end of try/ except/finally
#       i will run always at the end
#progam will now want the input again and again
