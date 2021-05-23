# list
list1 = [1,23,4]
list1.append(33)
list1.extend([5,6,7])
list1.pop()
print(list1)


# dict1 = {"hello":23}
# set1 = {1,1,1,1}
# print(set1)
# set.delete()

class Person():
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    def walk(self):
        print("walking")
        print(self.weight)
