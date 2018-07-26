#!/usr/bin/python
from collections import Counter
with open('task4.log') as kflog:
    numb = Counter(line.split(" - ", 1)[0] for line in kflog)
    for addr in numb.most_common(10):
      print("this IPaddress : %s was used - %s" % (addr[0], addr[1]))
