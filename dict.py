fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

mail = dict()  

fh = open(fname)
count = 0
for i in fh:
   word = i.split()
   if len(word) < 1 :
       continue
   if word[0] == "From" :
       mail[word[1]] = mail.get(word[1],0) + 1
       
bigname = None
maxname = None
key = 0
value = 0
for key,value in mail.items():
    if maxname == None or maxname < value:
        maxname = value
        bigname = key

print(bigname,maxname)

stuff = dict()
print(stuff['candy'])
