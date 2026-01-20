import requests as req
import pandas as pd
x = int(input("Enter a number: "))



print("You entered:", x)
print(x)
print("Hello, FunPy!")


y = []
for i in range(x):
    y.append(i)


print(y)
print("List of numbers from 0 to", x-1, ":", y)

data = {'Numbers': y}
df = pd.DataFrame(data)