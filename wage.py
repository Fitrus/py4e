 #Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

# try:
#     hours_worked = int(input("Please enter hours worked: "))
#     base_rate = 10
#     extra_rate = 15  # 10 * 1.5

#     if hours_worked > 40:
#         wage = 40 * base_rate + (hours_worked - 40) * extra_rate
#     else:
#         wage = hours_worked * base_rate

#     print("Pay:", wage)

# except ValueError:
#     print("Please enter a numerical value")

# #4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function.

hour = float(input("Hours: "))

rate = float(input("Rate: "))
extra_rate = rate*1.5

def computepay(hour,rate,extra_rate):
    if hour > 40:
        wage = 40 * rate + (hour - 40) * extra_rate
    else:
        wage = hour * rate
    return wage

print(computepay(hour,rate,extra_rate))
