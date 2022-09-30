weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f" You are {converted} pounds")
    
    ## guessing game
    
    secret_number  = 5
guess_number = 0
guess_limit = 3
while guess_number < guess_limit:
    guess = int(input("Guess: "))
    guess_number += 1
    if guess == secret_number:
        print("You Won")
        break
else:
    print("Sorry you've failed")
