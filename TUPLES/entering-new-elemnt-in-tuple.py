tuple1=(1,2,3,4,5,6,7)
print(f"The inserted tuple was: {tuple1}")
tuple1=tuple1+(8,)
print(f"After inserting an element the tuple becomes {tuple1}")

#ADDING ITEMS IN SPECIFIC INDEX
tuple1=tuple1[:3]+(78,79,80)+tuple1[4:]
print(f"\nAfter puting new tuple values in 4th index: {tuple1}")


