import numpy as np
import math
import csv
f=open('./20개씩묶고_컬럼별정규화.csv','r',newline='')
rdr=csv.reader(f)

data=[]
for j, i in enumerate(rdr):
    if(j!=0):
        data.append(i)
np.random.shuffle(data)

ratio = 0.75
count = int(math.ceil(len(data)*ratio))
print(len(data), count)
train = data[:count]
test = data[count:]

o1 = open('./trainset.csv','w',newline='')
wr1 = csv.writer(o1)
for i in train:
    wr1.writerow(i)

o2 = open('./test.csv','w',newline='')
wr2 = csv.writer(o2)
for i in test:
    wr2.writerow(i)
f.close()
o1.close()
o2.close()
