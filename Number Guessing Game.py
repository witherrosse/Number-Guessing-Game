import random
print("Welcome to the Guess number game ! ")
print("i'm thinking of a number from 1 to 100")
answer = random.randint(1,101)

difficulty_chose = input("Choose a difficulty level (easy,hard): ").lower()
is_game_over = False

attempt_remaining = 0
if difficulty_chose == "easy":
    attempt_remaining = 10
    print(f"you have {attempt_remaining} attempts remaining")
elif difficulty_chose == "hard":
    attempt_remaining = 5
    print(f"you have {attempt_remaining} attempts remaining")
else:
    print("Invalid input run again")
while not is_game_over:
    user_guess = int(input("Make a Guess : "))
    if user_guess > answer:
        print("too high")
        attempt_remaining -= 1
        print(f"you have {attempt_remaining} attempts remaining")
    elif user_guess < answer:
            print("too low")
            print(f"you have {attempt_remaining} attempts remaining")
            attempt_remaining -= 1
    elif user_guess == answer:
            print("Correct")
            is_game_over = True
    if attempt_remaining == 0:
        is_game_over = True
        print("you lose")
        print(f" the answer was {answer}")
























