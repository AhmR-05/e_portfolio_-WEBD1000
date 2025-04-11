#Author: Ashley Rose
#Student ID: W0516723
#Date: February 3rd, 2025
#Class: PROG 1700


print("Tax Deductions Calculator")

#Set salary and dependent variables for user input

salary = float(input("Please enter the full amount of your weekly salary :$ "))

dependent = int(input("How many dependents do you have?: "))

#Suggested step 3- setting variables for each rate

health = 0.27

ei = 0.22

ded_depend = 0.06 #deduction of dependent was 6%



total_health = salary * health
print(f"total health deduction is:${total_health} ")

total_ei = salary * ei
print(f"total ei deduction is:${total_ei} ")

total_depend = salary *(dependent * ded_depend)
print(f"total dependent deduction is:${total_depend}")

take_home = salary - (total_health + total_ei - total_depend)
print(f" Your total take home pay will be ${take_home}")
