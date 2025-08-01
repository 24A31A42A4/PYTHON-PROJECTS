import random
random_no=random.randint(1,50)
c=0
input_user=input("Guess the no with in range 1 to 50 Choose difficulty (easy/hard): : ")
if input_user=="easy":
    for i in range(1,11):
        print(f"You have a {11-i} attempts ")
        guessno=int(input("Guess the no : "))
        if guessno < random_no:
            print("You guessed is too low")
        elif guessno > random_no:
            print("You guessed is too high")
        else:
            print("Thats an Amazing man u guessed it ")
            c=1
            break
    if c==0:
        print(f"You've used all your chances. The number was {random_no}")
else:
    for i in range(1,6):
        print(f"You have a {6-i} attempts ")
        guessno=int(input("Guess the no :"))
        if guessno < random_no:
            print("You guessed is too low")
        elif guessno > random_no:
            print("You guessed is too high")
        else:
            print(f"Thats an Amazing man u guessed it the no is {random_no}")
            c=1
            break
    if c==0:
        print(f"You've used all your chances. The number was {random_no}")
    