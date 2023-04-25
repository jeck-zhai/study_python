## 算法，顾名思义，即为解决问题的步骤，算法的特征包括有穷性，确定性，可行性，有输入，有输出

# class Person:
#   def __init__(self, fname, lname):
#     print(self)
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     # print(self.firstname, self.lastname)
# x = Person("Bill", "Gates")
# # x.printname()


arr = [1, 5, 9, 8, 4, 10, 658, 4684, 2, 65]
# print(sorted(arr))
# print(sorted(arr, reverse=True))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort(arr))