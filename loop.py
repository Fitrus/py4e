# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.If the user enters anything
# other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest_num = None
smallest_num = None

while True:
    num = input("enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest_num is None:
            largest_num = num
        elif largest_num < num:
            largest_num = num

        if smallest_num is None:
            smallest_num = num
        elif smallest_num > num:
            smallest_num = num
    except:
        print ("invalid value")
        continue

print(largest_num)
print(smallest_num)