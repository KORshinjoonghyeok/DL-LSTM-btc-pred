import csv
f = open('./중복제거최종데이터_전처리전.csv', 'r', newline='')
rdr = csv.reader(f)
o = open('./타겟추가데이터2_새로운방식.csv', 'w', newline='')
wr = csv.writer(o)
wr.writerow(['time', 'low', 'high', 'open', 'close', 'volume', 'sma5', 'sma20', 'sma120', 'ema120', 'ema12', 'ema26', 'dn', 'mavg', 'up', 'pctB', 'rsi14', 'macd', 'signal', 'target_after6', 'target_after12', 'target_after18', 'target_after24'])

queue = []
for j,i in enumerate(rdr):
    if(j!=0):
        queue.append(i)
        if(j>4):
            data = queue.pop(0)
            data.append(queue[0][4])
            data.append(queue[1][4])
            data.append(queue[2][4])
            data.append(queue[3][4])
            wr.writerow(data)

f.close()
o.close()
