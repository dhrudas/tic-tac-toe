from random import randint

print("GHOST GAME!")
still_alive = True
score = 0

while still_alive:
    ghost_door = randint(1, 5)
    print("5 doors ahead...")
    print("A ghost behind one ...")
    print("Which door do you open?")
    door = input("1, 2, 3, 4 or 5?")
    answer = int(door)
    if answer  < 1 or answer  > 5:
        print("Wrong door!")
        continue

    if answer == ghost_door:
        print("GHOST!!!")
        still_alive = False
    else:
        print("No ghost!")
        print("You enter the next room...")
        score = score + 1

print("Game over! You scored: ", score)
