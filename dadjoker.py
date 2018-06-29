import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKES!")
header = colored(header, color="cyan")
print(header)

category = input("What type of dad joke do you want?")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": category}
).json()

num_of_jokes = res["total_jokes"]
results = res["results"]

if num_of_jokes > 1:
    print(f"There are {num_of_jokes} jokes about {category}")
    print(choice(results)["joke"])
elif num_of_jokes == 1:
    print("There's just one joke!")
    print(results[0]["joke"])
else:
    print(f"There are no jokes with that category: {category}")
