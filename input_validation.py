def user_input():

    # initial range choice
    number = "not a digit"

    # Acceptable values
    real_values = range(0, 11)

    # within range values
    within_range = False

    # check if number is valid or within range
    while number.isdigit() == False or within_range == False:
        number = input("Please enter a number between 0 to 10: ")

        # add an error message for digit check
        if not number.isdigit():
            print("\nCharacter entered is not a number!")

        # check for range
        if number.isdigit():
            if int(number) in real_values:
                within_range = True
            else:
                print("\nNumber entered not in range. Try again!")
                within_range = False

    return int(number)


result = user_input()
print(f"\nThe number you entered is {result}.")    