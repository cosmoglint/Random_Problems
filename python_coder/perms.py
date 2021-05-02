
lst = ["act","god","cat","dog","tac"]


mydict = {}


for i in lst:
    newl = [ x for x in i]
    thes = frozenset(newl)
    if thes not in mydict:
        mydict[thes] = 1
    else:
        mydict[thes] += 1

print(mydict)
