fname = input("Enter file name: ")
fh = open(fname)
sum = 0.00
count = 0.00
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        newline = line.strip()
        value = float(line[19: ].strip())
        sum = value + sum
        count = float(count +1 )
print("Average spam confidence: ", sum/count)