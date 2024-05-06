fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for i in fh:
   word = i.split()
   if len(word) < 1 :
       continue
   if word[0] == "From" :
       print (word[1])
       count = count+1

print("There were", count, "lines in the file with From as the first word")