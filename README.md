#### DL-LSTM-btc-pred
##### Data from coinmarketcap
---
##### LSTM에서 shuffle을 사용한 이유
![predbtc1](https://user-images.githubusercontent.com/71945157/95032319-04126280-06f5-11eb-9762-435a5c46ec61.png)
##### stateful=False 일경우 배치간 시계열성이 보장되므로 overfitting방지를 위해 shuffle을 사용.



##### result
![predbtc2](https://user-images.githubusercontent.com/71945157/95032699-851e2980-06f6-11eb-9e18-b0f514326ecc.png)

---

##### After
##### 딥러닝을 이용한 주식 자동매매 프로젝트를 위한 수정
---
###### Gdax API를 활용한 데이터 수집
###### unixtime(t) : 유닉스 시간대로 바꿔주는
![talib](https://user-images.githubusercontent.com/71945157/95061526-aacb2300-0736-11eb-8bbb-2c5306bed31f.png)

