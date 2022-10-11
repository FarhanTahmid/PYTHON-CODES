'''
kwargs return dictionary unlike args
'''

def myfunc(**kwargs):
    #if you want to test if kwargs return dictionary
    #print(kwargs)
    if 'fruit' in kwargs:
        print("My favorite fruit is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")

myfunc(fruit='apple', vegie='lettuce')

'''
ARGS AND KWARGS TOGETHER
'''
print("\nARGS AND KWARGS COMBINED IN A FUNCTION: ")
def myfunc2(*args,**kwargs):
    print(args)
    print(kwargs)
    print("\nI would like to have {} {}".format(args[0],kwargs['food']))

myfunc2(20,23,32, food='chickens', juice='lemon', fastfood='burger')
