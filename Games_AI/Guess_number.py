import random
number=random.randint(0,1000)
score=100000
invalid=0
chances=10

print("In this game you need to guess the correct number within 10 chances, else you lose")
while chances:
    guess=input("Enter your guess(1-1000): ")
    if guess.isdigit() and 0<=int(guess)<=1000:
        invalid=0
    else:
        print("Invalid entry")
        invalid=1
        while invalid==1:
            guess=input("Enter your guess(1-1000): ")
            if guess.isdigit() and 0<=int(guess)<=1000:
                invalid=0
            else:
                print("Invalid entry")
                invalid=1

    if number==int(guess):
        print("You have guessed the correct number")
        print("your score", score)
        exit()
    else:
        chances -= 1
        print("Wrong entry please try again")
        if number > int(guess):
            print("Hint: The number is greater than", guess)
        elif number< int(guess):
            print("Hint: The number is less than", guess )
        print("Chances left:", chances)
        score -= 10000

print("You Lose, You have used up all your chances")
print("The actual number is: " , number)