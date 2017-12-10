global pw
pw = "#Pass123!"

def pwcheck():
    passw = input("Enter the password : ")
    if (passw == pw):
        print("Password match")
    else:
        print("Wrong password.")

pwcheck()
