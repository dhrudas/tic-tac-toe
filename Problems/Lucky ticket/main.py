# Save the input in this variable
ticket = input()
ticket = list(ticket)

# read string and convert to list of int
# ticket = list(map(int, input()))
# Save the input in this variable
# ticket = list(map(int, input()))
# half1 = sum(ticket[:3])
# half2 = sum(ticket[3:])

# Add up the digits for each half
half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# using list comprehension
# half1 = sum(int(digit) for digit in ticket[:3])
# half2 = sum(int(digit) for digit in ticket[3:])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
