fname = input ("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhandle = open(fname)
    

hour = dict()
time_list = list()
for line in fhandle :
    new_line = line.rstrip().split()

    if len(new_line) == 0:
        continue

    if new_line[0] == "From":
        time = new_line[5]
        x = time.split(":")
        #print (x)
        hour[x[0]] = hour.get(x[0],0)+1

for k,v in hour.items():
    tmp = (k,v)
    time_list.append(tmp)

sorted_hour = sorted(time_list)
for h,count in sorted_hour:
    print(h,count)

#new_hour = dict()
#for k,v in hour.items():
#    new_hour = (v,k)
#    time_list.append(new_hour)

#print(time_list)

#sorted_hour = dict()
#sorted_hour = sorted(time_list, reverse = True)
#print (sorted_hour)



        



