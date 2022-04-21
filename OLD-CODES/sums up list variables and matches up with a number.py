
# Python3 program to find all pairs in  
# a list of integers with given sum  
  
from itertools import combinations 
  
def findPairs(lst, K):    
    res = [] 
    for var in combinations(lst, 2): 
        if var[0] + var[1] == K: 
            res.append((var[0], var[1])) 
          
    return res 
      
# Driver code 
lst = [1, 5, 3, 7, 9] 
K = 12
print(findPairs(lst, K)) 