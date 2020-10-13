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
#### 현재 진행상황
#### Talib으로 생성한 보조지표와 종가가격('Close')의 상관관계 시각화 
##### (각 volume,market cap, sma5,sma20,dn,ema12,ema26,mavg)
![talibTest33](https://user-images.githubusercontent.com/71945157/95432098-2b815d80-0989-11eb-9556-6494a260effb.png)

---
--- 
--- 
--- 
##### 이전 진행단계
##### Ta-lib을 이용한 보조지표 피처 생성(완성)
##### Gdax API를 이용한 데이터수집(완성)
##### 데이터셋 정규화(완성)
##### 데이터셋 분할(완성)
