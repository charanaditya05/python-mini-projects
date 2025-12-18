import random

choices=["snake","water","gun"]
print("Welcome to the game!")

computer=random.choice(choices)
user=input("Enter your choice snake,water,gun: ").lower()

if user not in choices:
    print("Invalid input!")
elif(computer==user):
    print("it's a tie.")
elif((computer=="snake" and user=="water") or (computer=="water" and user=="gun") or (computer=="gun" and user=="snake")):
    print(f"The computer has choosen {computer} and won!")
else:
    print(f"The player has choosen {user} and won!")
    print(f"The computer has choosen {computer} and lost!")