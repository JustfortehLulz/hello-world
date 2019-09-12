# Dice Rolling Simulator

import random as rand

answer = input("Do you want to roll a die? ")

while(answer == "Yes" or answer == "yes"):
    roll = rand.randint(1,6)
    print(roll)
    answer = input("Do you want to roll again? ")

print("Goodbye")
    
