UserNameInput = input("Enter your Username: ")
PasswordInput = input("Enter your Password: ")

if UserNameInput == "adminkrab" and PasswordInput == "4321":
    print("Welcome " + UserNameInput)
    print("1. Banana - 20 THB")
    print("2. Paper  - 3 THB")
    print("3. Gun    - 15000 THB")
    UserSelection = int(input("Enter what to buy: "))
    UserWanted = int(input("Enter how many you want to buy: "))
    if UserSelection == 1:
        print("Total : ",UserWanted*20,"THB")
    elif UserSelection == 2:
        print("Total : ",UserWanted*3,"THB")
    elif UserSelection == 3:
        print("Total : ",UserWanted*15000,"THB")
else:
    print("Invalid Username or Password")