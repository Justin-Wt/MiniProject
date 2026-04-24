import random
import os
import time

def delete():
    os.system('cls' if os.name == 'nt' else 'clear')

def randomize():
    blocks = []
    for _ in range(7):
        if random.randrange(0, 3+imputs*2) <=imputs+1:
            blocks.append("⬜")
        else:
            blocks.append("⬛")
    row = "".join(blocks)
    print(row)
    return row

def count_black(row):
    return row.count("⬛")

print("what difficulty you want to play?")
print("1.easy")
print("2.medium")
print("3.hard")
print("4.insane")
print("5.Expert")
print("6.Master")
print("7.Another")
imputs=int(input(">"))

while True:
    total_black = 0
    rows = []
    for i in range(4+imputs):
        r = randomize()
        rows.append(r)
        total_black += count_black(r)
    print("countdown in:")
    for count in range(5,0,-1):
    	print(count)
    	time.sleep(1)
    print("time is up")
    delete()
    print("Guess how many black blocks are there (type 'q' to quit)?")
    guess = input("Your guess: ")
    if guess.lower() == 'q':
        break

    try:
        guess = int(guess)
        if guess == total_black:
            print("✅ Correct!")
        else:
            print(f"❌ Nope. There were {total_black} black blocks total.")
    except ValueError:
        print("Please enter a number.")
    
    print()
    print("next game in:")
    for count in range(3,0,-1):
    	print(count)
    	time.sleep(1)
    delete()
