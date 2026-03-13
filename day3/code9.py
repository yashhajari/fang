# print(1,"",5)
# print(2,"",4)
# print(4,"",2)
# print(5,"",1)




for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i,"",j)