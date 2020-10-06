import csv
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import warnings

warnings.filterwarnings('ignore')

###20개씩 묶음(per day 4bars * 5days = 20bars)###
f = open('./타겟추가데이터2_새로운방식.csv', 'r', newline='')
rdr = csv.reader(f)

list = []
for i in rdr:
    list.append(i)

list.pop(0)
print(len(list))

gram_20 = []
for i in range(len(list) + 1 - 20):
    gram_20.append(list[i:i + 20])
gram_20 = np.array(gram_20)
print(gram_20.shape)

f.close()

###normalization###
o = open('./20개씩묶고_컬럼별정규화.csv', 'w', newline='')
wr = csv.writer(o)
title = ['time', 'low', 'high', 'open', 'close', 'volume', 'sma5', 'sma20', 'ema12', 'ema26', 'dn', 'mavg', 'up',
         'pctB', 'rsi14', 'macd', 'signal'] * 20
title.append('lastday_close')
title.append('after6ratio')
title.append('after12ratio')
title.append('after18ratio')
title.append('after24ratio')
wr.writerow(title)

scaler = MinMaxScaler(feature_range=(0, 1))  # scaler
for i in gram_20:
    close = np.array(i[-1][4], np.float64)  # -1 = lastIndex
    target = np.array(i[-1][-4], np.float64)
    ratio = target / close

    for j in range(1, i.shape[1] - 4):
        col = scaler.fit_transform(np.reshape(i[:, j], (-1, 1)))
        col = np.transpose(col)
        i[:, j] = col

    data = i[:, :-4]
    data = np.reshape(data, (-1))
    data = np.append(data, close)
    data = np.append(data, ratio)

    wr.writerow(data)
o.close()
