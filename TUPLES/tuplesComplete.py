#initializing a tuple
print("\nInitializing a tuple:")
tuple1=(1,2,3)
print(f"The initialized tuple is {tuple1}")
print(f"Length of the tuple is {len(tuple1)}")

#indexing
print("\nGrabbing elements and initializing:")
tuple2=('one',2.2, 300,"four", "farhan tahmid")
print(tuple2)
print(tuple2[2])
print(tuple2[-2])
print(tuple2[1:])
print(tuple2[2:4])

#counting value repeatation
print("\nCounting value repeatation:")
tuple3=('a','a','b', 3,3, 3,2,1)
print(tuple3)
print(tuple3.count('a'))
print(tuple3.count(3))
print(tuple2[1:])

#finding the index value
print("\nFinding the index value:")
print(tuple2.index(2.2))
print(tuple2.index('four'))
