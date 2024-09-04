print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_amount = 0

if size == "S":
    total_amount = 15
elif size == "M":
    total_amount = 20
else:
    total_amount = 25

if pepperoni == "Y":
    if size == "S":
        total_amount += 2
    else:
        total_amount += 3

if extra_cheese == "Y":
    total_amount += 1

print(f"Your final bill is: ${total_amount}.")