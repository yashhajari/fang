#wao to accept any character and check the entered character is
# upper cadse, lower case, digit and special symboal

ch = ord(input("Enter any character: "))  # convert character to ASCII

# ord function used to convert to ASCII code

if ch >= 65 and ch <= 90:   # A = 65 , Z = 90
    print("your entered character is in upper case")

elif ch >= 97 and ch <= 122:   # a = 97 , z = 122
    print("your entered character is in lower case")

elif ch >= 48 and ch <= 57:   # 0 = 48 , 9 = 57
    print("your entered character is digit")

else:
    print("your entered character is a special symbol")