import os
mylist= os.listdir(r'E:/demo1/')
for item in mylist:
    print(item)
    print(item[3:-19])
    print(item[6:-16])
