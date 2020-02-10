# import sys
from functools import reduce

list1 = [10,9,2,3,7,89,12,34,99,1]


res = reduce(lambda x,y: x if x>y else y,list1)
print(res)

# for i in sys.argv[1:]:
# 	list1.append(int(i))


# res = list(map(lambda x : x**2 , list1))
# print(res)

# print(reduce(lambda x,y : x+y,res))

# d = reduce(lambda x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))) 
# print(d)
# # fil = list(filter(lambda x: (x>=3), (1,2,3,4)))
# # print(fil)
# # mp = list(map(lambda x:x+x,fil))
# # print(mp)
# # d = reduce(lambda x,y: x+y, mp)
# # print(d)

# n = int(input("Enter a number : "))

# f = (lambda x : x + 2)(n)

# print(f)