dict1={"a":10,"b":2,"c":3}
str1=""
for i in dict1:
  str1=str1+str(dict1[i])+" "
  str2=str1[:-1]
print(str2[::-1])




list1 = [1,2,3]
list2 = list1
list3 = [1,2,3]
print(list1 == list3)
print(list1 is list3)
print(list1 == list2)
print(list1 is list2)


words= ("cracking", "lamp", "madam", "lusture", "anaconda", "kayak")

result = list(filter(lambda word: word == word[::-1], words))
print(result)



x=12
def f1(a,b=x):
  print(a,b)
x=15
f1(4)






def my_func(n):
  r = []
  t = sorted(n)
  for i in n:
    r.append(t.index(i))
  return r

n = [5, 1, 2, 1, 3, 6]
if __name__ == "__main__":
  print(my_func(n))



list1 = []
list2 = []
if (list1 is list2):
    print("yayy")




def oddsums(n):
    total=0
    result=[]
    for i in range(1,n+1):
        odd= 2*i-1
        total=total+odd
        result.append(total)
    return result

print(oddsums(5))





val1=28**0
val2=2.5
val3='123'
val4=int(val3)
print(val1+val2+val4)





class Person:
  def __init__(self, id):
    self.id = id

sam = Person(100)

sam.__dict__['age'] = 49

print (sam.age + len(sam.__dict__))





x = "abcdef"
i = "a"
while i in x:
  x = x[1:]
  print(i, end = " ")
