import random


def is_valid_input(input_number):
    if input_number.isnumeric():
        return True
    else:
        return False

def exit_game(input_number):
    if input_number.lower() == "exit":
        return True
    else:
        return False


random_number = random.randrange(1,100)
print(random_number)

count = 0
number = input("Guess the secret number between 1-100: ")
count = count + 1

if exit_game(number) == False:

    while is_valid_input(number) == False:
        if exit_game(number) == True:
            print("End of game")
            exit()
        number = input("Guess only numeric numbers between 1-100: ")
        count = count + 1

    while exit_game(number) != True and int(number) != random_number:
        if int(number) > random_number:
            print("The secret number is lower!")
            count = count + 1
            number = input("Guess the secret number again: ")
            while is_valid_input(number) == False:
                if exit_game(number) == True:
                    print("End of game")
                    exit()
                count = count + 1
                number = input("Guess only numeric numbers between 1-100: ")

        else:
            print("The secret number is higher!")
            count = count + 1
            number = input("Guess the secret number again: ")
            while is_valid_input(number) == False:
                if exit_game(number) == True:
                    print("End of game")
                    exit()
                number = input("Guess only numeric numbers between 1-100: ")
                count = count + 1

    print("You guessed right the secret number!")
    print(f"It took to you {count} number of guesses")
else:
    print("End of game")