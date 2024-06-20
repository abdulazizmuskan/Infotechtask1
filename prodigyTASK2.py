import random 
rnum=random.randint(1,10)
loop=True
while loop:
    guess=int(input("enter the guess"))
    if guess==rnum:
        print("you guessed it right")
       
    elif guess<rnum:
        print("random number is greater than guess")
    else:
        print("random number is lower than guesss")
