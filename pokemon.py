import random
from time import sleep


choices = ["Bulbusaur", "Squirtle", "Charmander"]

computer = random.choice(choices)

player = False
name = input("Hello, please enter your name: ")
print(f"Hello {name} welcome to pokemon battle game")
while player == False:
    choice = input("Please choose one of these Pokemons (Bulbasur / Charmander / Squirtle / stop ): ")
    if choice == computer:
        print("please wait....")
        sleep(1)
        print("Tie")
    elif choice == "charmander":
        if computer == "squirtle":
            print("please wait....")
            sleep(1)
            print("You Lose!")
        else:
            print("please wait....")
            sleep(1)
            print("You win!!")
    elif choice == "squirtle":
        if computer == "Bulbasaur":
            print("please wait....")
            sleep(1)
            print("you lose")
        else:
            print("please wait....")
            sleep(1)
            print("you win")
    elif choice == "Bulbusaur":
        if computer == "Charmander":
            print("please wait....")
            sleep(1)
            print("you lose")
        else:
            print("please wait....")
            sleep(1)
            print("you win")
    elif choice == "stop":
        print("Thankyou for playing ")
        player = True

    else:
        print("Invalid play")
