import random
import string
email_or_number=input("Enter mail: ")
username=''
for x in email_or_number:
    if(x=='@' or x=='.'):
        break
    else:
        username+=x
charCounter=True
for x in username:
    if(ord(x)>58 and ord(x)<126):
        charCounter=True
        break
    else:
        charCounter=False
        continue
if(charCounter):
    username=username+str(random.randint(10,10000))
else:
    s=random.randint(1,5)
    randomchars=''.join(random.choices(string.ascii_uppercase + string.digits, k=s))
    username=username+randomchars
print(username)