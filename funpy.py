x = int(input("Enter a number: "))

print("You entered:", x)
print(x)

y = []
for i in range(x):
    y.append(i)

print(y)
print("List of numbers from 0 to", x-1, ":", y)