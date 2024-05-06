import re

fname = input("Enter the file name:")

if len(fname) < 1:
    fname = ("regex_sum_2003407.txt")

fhandle = open(fname)

total = 0
count = 0
for line in fhandle:
    number = re.findall("[0-9]+", line)
    for num in number:
        total =total + int(num)


print(total)




