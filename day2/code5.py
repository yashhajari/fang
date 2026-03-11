#wap to accept 3 no and check max no and print
n1 = int(input("enetr n1: "))
n2 = int(input("enetr n2: "))
n3 = int(input("enetr n3: "))

if n1>n2:
    if n1>n3:
        print("n1 is max")
    else:
        print("n3 is max")

else:
    if n2>n3:
        print("n2 is max")
    else:
        print("n3 is max")