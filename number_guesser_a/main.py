import random #PEP8 -> 2 spaces between functions /imports


def validate_input(user_guess):
    if not user_guess.isdigit():
        print("Invalid input. Please try again. It should be a number")
        return False #since we are not in a loop, we won't use "continue"
        
        #continue ## DOn't forget that this should continue. it was a wrong input-> gave message -> continue the loop
        # else:  We don't need an else, since it checked all situations

    user_guess = int(user_guess)
    if user_guess > 100 or user_guess <  1:
        print("You guess is out of range. Please try again! It shoul be a number between 1 and 100")
        return False

    return True

def main():
    rand_num = random.randint(1, 100)
    score = 100

    while True:
        user_guess = input("Guess a number between 1 and 100: ")
        
        if user_guess == 'q':
            print(f"Thank you for playing! Goodbye!!!")
            break # if user_guess is 'q' we should btreak out of loop
        
        #Using the above cell function
        if not validate_input(user_guess): # if the input is not validated continue the loop
            continue  
        # after validating we convert it into an int
        user_guess = int(user_guess)

        if rand_num > user_guess:
            print(f"Your guess {user_guess} is lower. Please try again")
        elif rand_num < user_guess:
            print(f"Your guess {user_guess} is higher. Please try again")
        else:
            print("Congratulation. Your guess is correct!")
            print(f"your score is {score}")
            break # don't forget to break the loop , so it will quite.

        score -= 10 # in this block, it means the guess was not correct and player loses 10 points
        score  = max(score, 0)

# We use this guaring if someone imports our function, our main function
# wouldn't run from the script
#Only the functions that are defined in the main.py ??
if __name__ == '__main__':
    main()

#last line of code should be a /n new line
