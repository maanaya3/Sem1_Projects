#Marco Anaya
#init
import random
print("Hello, Welcome to guess random number!")
print("You have 3 tries!")
print("Are you ready?")
diff = input("Please select difficulty, Easy(e), Medium(m), Hard(h)")
if diff == "e":
    eguess = int(input("Enter a number between 1 and 10")) #interger
    esecret = random.randint(1,10) #interger
    if int(eguess) == esecret:
        print("You guessed the right number")
    elif int(eguess) >= esecret:
        print("You lost because your number was too large")
    else: print("You lost because your number was too small")
    if int(eguess) != esecret:
        print ("Try again!")
        eguess2 = int(input("Enter a number between 1 and 10"))
        esecret2 = random.randint(1,10) #interger
        if int(eguess2) == esecret2:
            print("You guessed the right number")
        elif int(eguess2) >= esecret2:
            print("You lost because your number was too large")
        else: print("You lost because your number was too small")
        if int(eguess2) != esecret2:
                print ("Try again!")
                eguess3 = int(input("Enter a number between 1 and 10"))
                esecret3 = random.randint(1,10) #interger
                if int(eguess3) == esecret3:
                    print("You guessed the right number")
                elif int(eguess3) >= esecret3:
                    print("You ran out of lifes because your number was too large")
                else: print("You ran out of lifes because your number was too small")
        else: print("Thank you for playing!")
    else: print("Thank you for playing!")

if diff == "m":
    mguess = int(input("Enter a number between 1 and 25")) #interger
    msecret = random.randint(1,25) #interger
    if int(mguess) == msecret:
        print("You guessed the right number")
    elif int(mguess) >= msecret:
        print("You lost because your number was too large")
    else: print("You lost because your number was too small")
    if int(mguess) != msecret:
        print ("Try again!")
        mguess2 = int(input("Enter a number between 1 and 25"))
        msecret2 = random.randint(1,25) #interger
        if int(mguess2) == msecret2:
            print("You guessed the right number")
        elif int(mguess2) >= msecret2:
                print("You lost because your number was too large")
        else: print("You lost because your number was too small")
        if int(mguess2) != msecret2:
            print ("Try again!")
            mguess3 = int(input("Enter a number between 1 and 25"))
            msecret3 = random.randint(1,25) #interger
            if int(mguess3) == msecret3:
                print("You guessed the right number")
            elif int(mguess3) >= msecret3:
                    print("You ran out of lifes because your number was too large")
            else: print("You ran out of lifes because your number was too small")
        else: print("Thank you for playing!")
    else: print("Thank you for playing!")

if diff == "h":
    hguess = int(input("Enter a number between 1 and 100")) #interger
    hsecret = random.randint(1,100) #interger
    if int(hguess) == hsecret:
        print("You guessed the right number")
    elif int(hguess) >= hsecret:
        print("You lost because your number was too large")
    else: print("You lost because your number was too small")
    if int(hguess) != hsecret:
        print ("Try again!")
        hguess2 = int(input("Enter a number between 1 and 100"))
        hsecret2 = random.randint(1,100) #interger
        if int(hguess2) == hsecret2:
            print("You guessed the right number")
        elif int(hguess2) >= hsecret2:
            print("You lost because your number was too large")
        else: print("You lost because your number was too small")
        if int(hguess2) != hsecret2:
                print ("Try again!")
                hguess3 = int(input("Enter a number between 1 and 100"))
                hsecret3 = random.randint(1,100) #interger
                if int(hguess3) == hsecret3:
                    print("You guessed the right number")
                elif int(hguess3) >= hsecret3:
                        print("You ran out of lifes because your number was too large")
                else: print("You ran out of lifes because your number was too small")
        else: print("Thank you for playing!")
    else: print("Thank you for playing!")
