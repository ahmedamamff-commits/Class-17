import random #importing module
playing = True #initialize
number = str(random.randint(0,1000)) #random built in function

print("I will generate a random number between 0 and 1000. You have to guess it.")
print("The game ends when you get 1 hero!")
#iterate the loop while condition is true
while playing:
    guess = input("Enter your guess:")
    if number == guess:
        print("You won the game and got a hero!")
        print("The number was:", number)
        break

    else:
        print("Your guess wasn't quite right. Try another guess.")