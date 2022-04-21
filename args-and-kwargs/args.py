"""USES OF ARGS,
LETS WRITE A NORMAL FUNCTION
"""
def sumofnumbers(a,b):
    '''
    function returns 5% of the sum of a and b
    '''
    return sum((a,b))*0.05
c=sumofnumbers(20,40)
print(f"\nThe 5% of the sum of a and b is {c}")

'''
THERE IS A LIMITATION USING THE SUM FUNCTION
WE CAN ONLY PASS TWO PARAMETERS HERE CZ SUM ALLOWS ONLY TWO PARAMETERS
SO FOR THIS WEE NEED *args
'''

print("\nUSING ARGS:")
def sumofnumbers2(*args):
    """
    Will take multiple input now
    """
    return sum(args) * 0.05
d=sumofnumbers2(40.45,60,56,3444,3,33)
print(f"The 5% of the sum of all the arguments: {d}")

'''
if we dont use args here there will be a traceback:
'''
print("\nTraceback: ")
def sumofnumbers(a,b,c=0,d=0,e=0,f=0):
    '''
    function returns 5% of the sum of a and b
    '''
    return sum((a,b,c,d,e,f))*0.05
c=sumofnumbers(20,40,50,30,45,60,70)
print(f"\nThe 5% of the sum of a and b is {c}")

'''
here the traceback comes because we have 6 positions open in the function for parameters. But 7
arguments were passed. So if we are passing many arguments, for that
we need to use *args so that we dont have to pass parameters as much as arguments we pass
'''
'''
ARGS RETURN TUPLE
'''

