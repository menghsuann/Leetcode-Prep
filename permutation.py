#function
def toString(List):
    return ''.join(List)
def permute(a, l, r):
    if l == r:
        print toString(a)
    else:
        for i in xrange(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l] # backtrack
  
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

#https://www.geeksforgeeks.org/python-program-to-print-all-permutations-of-a-given-string/


#inbuilt function
from itertools import permutations
import string
  
s = "ABCD"
a = string.ascii_letters
p = permutations(s)

d = []
for i in list(p):
    if (i not in d):
        d.append(i)
        print(''.join(i))
