import random

guesses = 0

top_of_range = input("Type the max number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter a number grater than 0 next time, or it would'n continue.")
        quit()

else:
    print("Enter a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Enter your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Enter a number.")
        continue

    if random_number == user_guess:
        print("You got it.")
        break
    elif user_guess > random_number:
        print("Try to enter a smaller number.")
    else:
        print("Try to enter a bigger number.")

print()
print(f"You choose range between 0 and", top_of_range)
print(f"The right number is:", random_number)
print()
print(f"-CONGRATULATIONS!- You finally got it after ", guesses, " guesses.")
print()