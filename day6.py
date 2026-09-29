# if else statement or decison making statement


# suppose
# correct email: abc@gmail.com
# correct password: abcdefgh


email =input("enter your email here: ")

if '@' in email:
    password = input("enter your password here: ")

    if email == "abc@gmail.com" and password == "abcdefgh":
        print('welcome you are logged in')

    elif email=="abc@gmail.com" and password !="abcdefgh":
        print("you enter wrong password try again")
        password = input("please enter your password again")
        
        if password =="abcdefgh":
            print("finally correct you are logged in now")
        else:
            print("still incorrect")

    else:
        print("please enter correct credentials")


else:
    print('incorrect email try again')


