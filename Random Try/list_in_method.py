list1=['1','2','3']
list2=['3','2']

for item in list1:
    if item not in (list1 and list2):
        print(item)
    elif item in (list1 and list2):
        print(f"found {item}")