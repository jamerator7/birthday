from datetime import date
import time
print("Welcome")
name = input("What is your name")
m = input("Enter your birth month: ")
d = input("Enter your birth day: ")
y = input("Enter your birth year: ")
print("Your birthday is: " + m + "-" + d + "-" + y)

for i in range(3):
    print("happy birthday to you")
    time.sleep(1)

print("Happy Birthday dear " + name)

td = str(date.today())
td_arr = td.split("-")
cy = td_arr[0]
cm = td_arr[1]
cd = td_arr[2]
print(cy + "-" + cm + "-" + cd)
time.sleep(2)