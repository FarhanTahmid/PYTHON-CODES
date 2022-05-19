#using open function to read the content of a file
#by default the mode is reading which is 'r'
import nt

f=open('textFile.txt','r')
data=f.read()
print(data)
f.close()
g=open("textFile.txt",'r')
rdata=g.read(6) #reads only 6 letters
print(rdata)
g.close()
h=open("textFile.txt",'r')
lineData=h.readline() #reads only one line in the file, prints until it finds the line ending character
print(lineData)
secondLineData=h.readline()
print(secondLineData)
h.close()

#writing files in python
i=open('writeText.txt','w') #this will completely rewrite the file and will remove all the existing things
i.write("i just don't want to loose her")
i.close()

#appending files
j=open("textFile.txt",'a')#will append typing in the last of the line
j.write("\nMan i want to be with her for the rest of my life :'))")
j.close()

#you can open a file by 'with' statement, thus you dont need to close all the time
with open("writeText.txt",'a')as f:
    f.write("This is farhan")

#check whether something is present in the file or not
k=open("textFile.txt",'r')
l=k.read()
if "Fizanaz" in l:
    print("fiza is in farhan's life")
else:
    print("Fiza is still in farhan's life")