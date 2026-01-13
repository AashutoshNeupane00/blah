#game
import random
print("Why did the chicken cross the road?")
answers = [
    "To get to the other side!",
    "Because it was free-range!",
    "To escape the farmer!",
    "To prove it wasn't chicken!",
    "To find some eggs-citing adventures!"
]   
print(random.choice(answers))
print("Do you want to hear another answer? (yes/no)")
while True:
    user_input = input().strip().lower()
    if user_input == "yes":
        print(random.choice(answers))
        print("Do you want to hear another answer? (yes/no)")
    elif user_input == "no":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")
        