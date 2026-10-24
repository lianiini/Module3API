import requests
import random

baseurl = "https://pokeapi.co/api/v2/pokemon/"

randomnumber = str(random.randint(1,10))

finalurl = baseurl + randomnumber

pokemon = requests.get(finalurl).json()

name = pokemon['name']
weight = pokemon['weight']
height = pokemon['height']

guessCount = 3
while True:
    if guessCount != 0:
        print("Guess that pokemon!")
        guess = input(f"{name}\nWeight: {weight}\nHeight: {height}\nGuess [exit to quit]: ")
        if guess == name:
            print("You guessed it!")
            break
        elif guess == "exit":
            break
        elif guess != name:
            guessCount-=1
            print(f"Wrong guess! Guess Left: {guessCount}")
        else:
            print("Wrong guess! Try Again!")
    else:
        print(f"You ran out of guesses!\nThe answer is {name}")
        break
