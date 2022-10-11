#dictionary initializing
print("\nIniitializing Dictionary:")
dict1={'key1':'value1','key2':'value2'}
print(dict1)

#getting value from dictionary
print("\nGetting value from dictionary:")
print(dict1['key1'])

#list in dictionary
print("\nList in dictionary:")
dict2={'k1':123,'k2':[0,1,'a',"im a stranger"],'k3':{'nestedkey':100}}
print(dict2)
print("Getting value frome the list:")
print(dict2['k2'])
print("Getting value from the nested dictionary:")
print(dict2['k3']['nestedkey'])
print("Getting value from the list:")
print(dict2['k2'][2])
print("Uppercasing a letter in the nested list inside the dictionary:")
print(dict2['k2'][3].upper())
print("As dictionary is immutable unlike lists the dictionary remains the same as initialized at first:")
print(dict2)

#assigning new key and value to a dictionary
print("\nAssigning new key and value to a dictionary:")
dict3={'k1':100,'k2':"farhan"}
print(dict3)
dict3['k3']='ishrak'
print(dict3)

#changing the value of a key
print("\nChanging the value of a key:")
dict3['k3']= 'Tahmid'
print(dict3)

#showing all the keys, items and values in a dictionary
print("\nShowing all the keys and values in a dictionary:")
print("Keys:")
print(dict1.keys())
print(dict2.keys())
print(dict3.keys())
print("\nValues:")
print(dict1.values())
print(dict2.values())
print(dict3.values())
print("\nItems:")
print(dict1.items())
print(dict2.items())
print(dict3.items())

print("\nAnother dictionary initialization:")
dict4={1:'apple',2:'juice'}
print(dict4)