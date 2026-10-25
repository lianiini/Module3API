import requests
import random

baseurl = "https://pokeapi.co/api/v2/pokemon/"

randomnumber = str(random.randint(1,30))
randomAbility = random.randint(0,1)

finalurl = baseurl + randomnumber

print("Connecting to PokéAPI...")
response = requests.get(finalurl)

# Use an if-else statement to check if the request was successful
if response.status_code == 200:
    pokemon = response.json()

    name = pokemon['name']
    weight = pokemon['weight']
    height = pokemon['height']
    ability = pokemon['abilities']
    randomAbi = ability[randomAbility]['ability']['name']

    guessCount = 3
    while True:
        if guessCount != 0:
            print("\nGuess that pokemon!\n")
            guess = input(f"Weight: {weight}\nHeight: {height}\nAbility: {randomAbi}\n\nGuess ['exit' to end game]: ")
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
else:
    print(f"Failed to fetch data from the API. Server returned status code: {response.status_code}")
