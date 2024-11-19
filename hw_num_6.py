
import random
#START Question 1
one_name: str = str(input("first name: "))
two_name: str = str(input("last name: "))
tree_name: str = str(input("tree name: "))
four_name: str = str(input("four name: "))

lottery_name: str = random.choice([one_name, two_name, tree_name, four_name])
print(f'the winner name is : {lottery_name}')
#END

#START Question 2
number: int = int(input("Type a number between 100 and 1 :"))
random_number: int = random.randint(1, 100)
print({random_number})

attempts: int = 1
while True:
    if number < random_number:
        number: int = int(input("Too low, try a larger number: "))
        attempts += 1
    elif number > random_number:
        number: int = int(input("Too high, try a smaller number: "))
        attempts += 1
    else:
        print("You are the winner!")
        print(attempts)
        break
#END

#START Question 3
total_temperature = 0
for i in range(1, 6):
    while True:
        temp: float = float(input(f"Enter the temperature for city {i}: "))
        if -50 <= temp <= 45:
            total_temperature += temp
            break
        else:
            print("Invalid temperature! Please enter a temperature between -50 and 45.")

average_temperature = total_temperature / 5
print(f"The average temperature of the 5 cities is: {average_temperature:.}")
#END

#START Question 4
num: int = int(input("Enter a number:"))

for i in range(0, num+1):
    for g in range(1, i + 1):
        print(g, end="")
    print()
for i in range(num-1, 0, -1):
    for g in range(1, i + 1):
        print(g, end="")
    print()
#END

#START Question 5
num: int = int(input("Enter a number: "))

for i in range(1, num + 1):
    print(" " * (num - i), end="")
    print("*" * (2 * i - 1))
#END

#START Question 6
    count = 0
    while True:
        try:
            num: int = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if num % 11 == 0:
            break
        elif num % 7 == 0:
            count += 1
        else:
            print(f"The number of numbers entered that are divisible by 7:{count}")
            break
#END

#START Question 7
num: int = int(input("Enter a number"))

if num % 5 == 0 and num % 3 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Buzz")
elif num % 5 == 0:
    print("Fizz")
#END

