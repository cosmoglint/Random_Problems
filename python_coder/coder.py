def f(x = 100, y = 100):
 return(x+y, x-y)
x, y = f(y = 200, x = 100)
print(x, y)


lst = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(lst)-1, -1, -1):
    print( lst[i] , end = ' ')


def my_func(n, i, j):
  a, b = n.index(i), n.index(j)
  return a, b


n = [2, 4, 8, 10, 8, 12]
i = 8
j = 1

if __name__ == "__main__":
  a, b = my_func(n, i, j)
  print(a, b)
