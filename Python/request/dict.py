# 把一个字典的[key]写成list1
# 他的:val写成list2
# 那么我如何生成字典？

# dict.update({[list1]:list2})


# for i in range(len(list1)):#因为两个列表大小一样
#    dict.update({list1[i]:list2[i]})

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

for i in range(len(list1)):
    print(list1[i])
    print(list2[i])
    print("i=%s"%(i))