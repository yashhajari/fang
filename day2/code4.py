#wap to accept 5 number in 5 different variable and check maximum value and print using simple if
v1 = int(input("enter v1:"))
v2 = int(input("enter v2:"))
v3 = int(input("enter v3:"))
v4 = int(input("enter v4:"))
v5 = int(input("enter v5:"))

if v1>v2 and v1>v3 and v1>v4 and v1>v5:
    print(" v1 is greater")
    
if v2>v1 and v2>v3 and v2>v4 and v2>v5:
    print(" v2 is greater")

if v3>v1 and v3>v2 and v3>v4 and v3>v5:
    print(" v3 is greater")

if v4>v1 and v4>v2 and v4>v3 and v4>v5:
    print(" v4 is greater")

if v5>v1 and v5>v2 and v5>v3 and v5>v4:
    print(" v5 is greater")


