# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)

#output:
#0
#1
#8
#27
#64
#125
#216
#343
#512
#729

### fibonacci sequence

def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)


#output:
#1
#1
#2
#3
#5
#8
#13
#21
#34
#55

##if this code were a normal func it will be like :













def fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b,a+b

    return output


fibon(10)
