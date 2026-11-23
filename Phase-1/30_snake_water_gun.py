'''
1 for snake 
-1 for water 
0 for gun 
'''
import random
youDict = {
    "s":1,
    "w":-1,
    "g":0
}
computerChoice = random.randint(-1,1)
you = input("Enter your choice: ").lower()
if you in youDict:
    yourChoice = youDict[you]

    if yourChoice == computerChoice:
        print(f"{yourChoice} and {computerChoice} : draw")
    elif (yourChoice == 1 and computerChoice == -1) or \
        (yourChoice == -1 and computerChoice == 0) or \
            (yourChoice == 0 and computerChoice == 1):
         print(f"{yourChoice} and {computerChoice} : you win")
    else:
        print(f"{yourChoice} and {computerChoice}: Computer wins")
else:
    print("Invalid choice! Please enter s, w, or g.")

