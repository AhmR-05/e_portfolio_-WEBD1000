#Compound interest calculator

#from BroCode on youtube, added modifications

principle = 0

rate = 0

time = 0

print("Compound Interest Calculator")
print("----------------------------")

name = input("Please enter your name: ")

while principle <= 0:
    principle = float(input("Enter the principle amount:$ "))
    
    if principle <= 0:
        print("The principle cannot be less than or equal to zero.")


while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    
    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero.")
        

while time <= 0:
    time = int(input("Enter the time in years: "))
    
    if time <= 0:
        print(" Time cannot be less than or equal to zero")

print(f"The principle amount is ${principle}.")
print(f"The interest rate is {rate}")
print(f"The time is {time} year(s)")

total = principle * pow((1 + rate / 100), time)

print(f"{name}, your balance after {time} year(s) will be ${total:.2f}")


