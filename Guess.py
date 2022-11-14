secret_number = input("Enter the number you want other player to guess(Number must be between 0 and 9):")
secret_number_length = len(secret_number)
guess_count = 0
guess_limit = 3
if secret_number_length==1:
    while guess_count<guess_limit:
        guess = int(input("Guess the number: "))
        guess_count += 1
        if guess == int(secret_number):
            print("You Won!")
            break
    else:
        print("You Ran Out Of Attempts!")
else:
    print("Please enter valid number")