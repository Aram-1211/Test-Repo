password = input("Input Password: ")
validity = True
length = len(password)
if length < 8:
    validity = False

i = 0 
SameChar = True
if password[i].isdigit() == True:
    for i in range(1, length, 1):
        if password[i].isdigit == False:
            SameChar = False
            break
        i += 1
else:
    for i in range(1, length, 1):
        if password[i].isdigit() == True:
            SameChar = False
            break
        i += 1
        
        

if SameChar == True:
    validity = False

if validity == True:
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")