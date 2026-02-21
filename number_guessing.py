import random

top_of_range = input("Please type a number: ")
if top_of_range.isdigit():
   top_of_range = int(top_of_range)

   if top_of_range <= 0:
       print("Please enter a number greater than 0")
       quit()
else:
    print("Please enter a number next time!")
    quit()

random_number = random.randint(0,top_of_range)
print(random_number)

guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please enter a number next time!")
        continue
    if user_guess == random_number:
        print("Correct!")
        break

    elif user_guess > random_number:
            print("Your guess is too high!")
    else:
            print("Your guess is too low!")


print("You got it in", guess,  " guesses!")
