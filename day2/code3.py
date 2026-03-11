#wap to accept three paper marks and calculate total marks, percentage and 
# check if percentage is greater then or equal to 60 thr he/she is eligible for placement
print("enter marks out of 100")
marks1 =int(input("enter marks of sub 1:"))
marks2 =int(input("enter marks of sub 2:"))
marks3 =int(input("enter marks of sub 3:"))

total = marks1+marks2+marks3
percent = total/3.0
print("Total=", total)
print("percentage=", percent)

if percent >= 60:
    print("you are eligible for placemnet")
    
else:
    print("feilding set")