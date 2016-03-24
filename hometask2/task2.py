#!/usr/bin/python
kfstring = "Wow Abba Wow"

def p1(st):
     return st.lower() == st[::-1].lower()
print(p1(kfstring))
