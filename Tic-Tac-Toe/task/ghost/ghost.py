from random import randint

print("GHOST GAME!")
still_alive = True
score = 0

while still_alive:
    ghost_door = randint(1, 7)
    print("7 doors ahead...")
    print("A ghost behind one ...")
    print("Which door do you open?")
    door = input("1, 2, 3, 4 , 5 , 6 or 7?")
    answer = int(door)
    if answer  < 1 or answer  > 7:
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
