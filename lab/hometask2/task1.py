#!/usr/bin/python
kflist1 = [1,2,3,4,5,6,7]
kflist2 = ['a','b','c','d']
def d1(l1, l2):
    return  dict(zip(l1,l2 +[None]*(len(l1)-len(l2))))
print(d1(kflist1,kflist2))
