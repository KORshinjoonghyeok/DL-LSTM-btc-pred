import gdax
from datetime import datetime
import csv
import time

def unixtime(t):
    temp = t.split('-')
    return  int(time.mktime(datetime(int(temp[0]), int(temp[1]), int(temp[2])).timetuple()))

public_client = gdax.PublicClient()
o = open('../webCrawling/get_bitcoin_data.csv', 'a', newline='')
wr = csv.writer(o)

granularity = 3600*6 #6H
interval = 3600*24*50
start_time = '2015-02-28'
last_time = '2020-10-05'

result = []

for i in range(unixtime(start_time), unixtime(last_time), interval):
    start = str(datetime.fromtimestamp(i)).split(' ')[0]
    if i + interval > unixtime(last_time):
        end = str(datetime.fromtimestamp(unixtime(last_time) + 3600*24)).split(' ')[0]
    else:
        end = str(datetime.fromtimestamp(i+interval)).split(' ')[0]

    r = public_client.get_product_historic_rates('BTC-USD', start=start, end=end, granularity=granularity)
    for k in r:
        result.append([str(datetime.fromtimestamp(k[0])), k[1], k[2], k[3], k[4], k[5]])

    last_r_size = len(r)
    print(last_r_size)


popped = result.pop(-1 * last_r_size)
print('del', popped)
for i in result:
    wr.writerow(i)

o.close()

f = open('./get_bitcoin_data.csv', 'r', newline='')
rdr = csv.reader(f)
dic = {}
for i in rdr:
    key = str(i[0])
    value = str(i[1]) + ' ::: ' + str(i[2]) + ' ::: ' + str(i[3]) + ' ::: ' + str(i[4]) + ' ::: ' + str(i[5])
    dic[key] = value
f.close()

o = open('./duplication_eliminated_bitcoin_data.csv', 'w', newline='')
wr = csv.writer(o)
wr.writerow(['time','low','high','open','close','volume'])

for i in dic:
    temp = dic[i].split(' ::: ')
    temp.insert(0,i)
    wr.writerow(temp)

o.close()