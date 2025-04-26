# import the art
from high_follower_art import logo, vs
import random

# load the game data from a file
from game_data import data


# format the account data
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_description}, from {account_country}"


# print the logo
print(logo)
score = 0

# set the game flag to True
game_on = True
# generate and select a random account
account_b = random.choice(data)
print("-----------------------------------------------")
print(f"Welcome to the Follower Count Comparison Game!")
print("-----------------------------------------------")

# start the game loop
while game_on:

    # making account at position B becomes the next account at position A
    account_a = account_b
    # generate a new random account for position B
    account_b = random.choice(data)

    # compare account
    if account_a == account_b:
        account_b = random.choice(data)

    print(
        f"Compare these two accounts:\n{format_data(account_a)}\n{vs}\n{format_data(account_b)}"
    )

    # ask the user for their choice
    choice = input("\nWho has more followers? (a/b): ").lower()

    if choice == "a" and account_a["follower_count"] > account_b["follower_count"]:
        print("----------------------------")
        print("Correct!")
        score += 1
    elif choice == "b" and account_b["follower_count"] > account_a["follower_count"]:
        print("----------------------------")
        print("Correct!")
        score += 1
    else:
        print("----------------------------")
        print(
            "Wrong! The correct answer is:",
            "a" if account_a["follower_count"] > account_b["follower_count"] else "b",
        )

    # print the current score
    print(f"Your current score: {score}")
    print("----------------------------")

    print()
    # wait for a moment before asking the next question
    input("\nPress Enter to continue...")
    # check if the user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        game_on = False

# print the final score after the game ends
print("----------------------------")
print("Game over! Your final score is:", score)
print("----------------------------")
