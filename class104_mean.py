# Data - 10,15,20,20,30,10,17,10
# 10,10,10,15,17,20,20,35
#mean = (10+15+20+30)/4
#print(mean)


#from collections import Counter
#new_data = "Whitehatjr"
#data = Counter(new_data)
#print(data)

#new_list =  data.items()
#print(new_list)

#value = data.values()
#print(value)

import csv
with open('height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n=len(new_data)

total=0
for x in new_data:
    total+=x
mean=total/n
print("Mean/ Average is :" + str(mean))