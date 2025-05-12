import random
# Choose Difficulty Level
print("Welcome to the Number Guessing Game!")
attempts=0
def secret_num():
    global attempts,difficulty
    while True:
        difficulty=input("Choose difficulty level(Easy, Medium, Hard): ").lower()
        if difficulty=="easy":
            secret_number=random.randint(1,50)
            attempts=10
            return secret_number
        elif difficulty=="medium":
            secret_number=random.randint(1,100)
            attempts=7
            return secret_number
        elif difficulty=="hard":
            secret_number=random.randint(1,200)
            attempts=5
            return secret_number
        else:
            print("Invalid input. Please choose Easy, Medium, or Hard.")

def call():
    global secret_number
    secret_number=secret_num()
    print(f"You have {attempts} attempts to guess the number.")
    print("Good luck!")

call()
# Hint for the player
print("Here's a hint for you.")
if secret_number%2==0:
    print("Hint: The secret number is even.")
else:
    print("Hint: The secret number is odd.")

# Main function for the game
def number_guessing_game():
    i=0
    global attempts,secret_number
    while i<attempts:
        if difficulty=="easy":
            num=int(input("Guess the secret number between 1 and 50: "))
        elif difficulty=="medium":
            num=int(input("Guess the secret number between 1 and 100: ")) 
        elif difficulty=="hard":   
            num=int(input("Guess the secret number between 1 and 200: "))
        if num<secret_number:
            print("Too Low! Try Again.")
        elif num>secret_number:
            print("Too high! Try Again.")       
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        if i==attempts-1:
            print("Sorry! You've used all your attempts. The secret number was", secret_number)
            break
        i+=1
        

# Call the function to start the game
number_guessing_game()

#Retry the game
retry=(input("Do you want to play again? (yes/no): ")).lower()
if retry in ["yes","y","yep"]:
    attempts=0
    call()
    number_guessing_game()
else:
    print("Thank you for playing!")