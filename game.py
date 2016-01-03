from random import randint
import time


print("Hello!")

time.sleep(1)

print("Welcome to Guess Games!")
print("")

time.sleep(1)

name = input("Enter your name:")

time.sleep(1)

rand = randint(1, 10)
user_no = 0


while user_no != rand:

    print("")
    number = input("Enter Number:")
    user_no = int(number)

    if user_no == rand:

        print("")
        print("Yay!")
        print("You got it " + name + "!")
        time.sleep(1)
        print("Bye!")
        time.sleep(2)

    else:

        if user_no > rand:

            print("Your number is greater")
            time.sleep(1)

        else:

            print("Your number is lesser")
            time.sleep(1)

