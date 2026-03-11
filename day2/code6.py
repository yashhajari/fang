#else if ladder 

# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     default

# #wap to if percent is greater then 90 so assign grade a if greater than 80 assign b 
# and if percent is greater than 60 so assign grade c and if percent is below 60 print fail

marks = int(input("Enter percentage: "))

if marks>=90:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade B")
else:
    print("Fail")