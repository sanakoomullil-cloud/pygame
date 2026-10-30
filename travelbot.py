import re, random
from colorama import Fore, init

init(autoreset=True)
destinations= {
    "beaches": ["bali", "maldeves", "phuket"],
    "mountains": ["swiss alps", "rocky mountains", "himalay"],
    "cities": ["tokoyo", "paris", "new york"]

}
jokes=[
    "why dont programmers like nature? too many bugs",
    "why did the computer go to the doctor?because it had a virus",
    "why do travelers always feel warm? because of all their hot spots"
]
def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())


def recommend():
    print(Fore.CYAN +"travelBot: beaches, mountain, or cities?")
    preference=input(Fore.YELLOW+"you:")
    preference=normalize_input(preference)

    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.GREEN+f"TravelBot  : how about {suggestion}?")
        print(Fore.CYAN+"TravelBot: do you like it? (yes/no)")
        answer=input(Fore.YELLOW+"you:").lower()

        if answer =="yes":
            print(Fore.GREEN+f"TravelBot: awesome! enjoy {suggestion}")
        elif answer=="no":
            print(Fore.RED+"TravelBot: lets try another")
        else:
            print(Fore.RED+"TravelBot: I'll suggest again")
    else:
        print(Fore.RED+"TravelBot: sorry, i dont have that type of destination")
        recommend()

def packing_tips():
    print(Fore.CYAN+"TravelBot: where to?")
    location=normalize_input(input(Fore.YELLOW+"you"))
    print(Fore.CYAN+"TravelBot: how many days")
    days=input(Fore.YELLOW+"you")

    print(Fore.GREEN +f"TravelBot: packing tips for {days} days in {location}")
    print(Fore.GREEN +"- pack versatile clothes")
    print(Fore.GREEN+"-bring chargers/apapters")
    print(Fore.GREEN+"-check the weather forecast")
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()

