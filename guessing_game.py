import random


def is_valid_input(input_number):
    if input_number.isnumeric():
        return True
    else:
        return False

# def exit_game(input_letter):
#
#     if guessed_number.lower() == "exit":
#         return  True
#     return guessed_number

random_number = random.randrange(1,100)
print(random_number)
number = input("Guess the secret number between 1-100: ")
# result = exit_game(number)


while is_valid_input(number) == False:
    number = input("Guess only numeric numbers between 1-100: ")

while int(number) != random_number:

    if int(number) > random_number:
        print("The secret number is lower!")
        number = input("Guess the secret number again: ")
        while is_valid_input(number) == False:
            number = input("Guess only numeric numbers between 1-100: ")

    else:
        print("The secret number is higher!")
        number = input("Guess the secret number again: ")
        while is_valid_input(number) == False:
            number = input("Guess only numeric numbers between 1-100: ")

print("You guessed right the secret number!")
