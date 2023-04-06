# coding:utf-8

#连续两天同号概率1/16
#每次投注另外15个号，中奖概率15/16
#剩下全部按赔率压
#pay1*rate1／15 + pay2*rate2／15 + pay3*rate3／15 + ...
#rate1*rate1/15



lottery_rate=(12,
22,
21,
23,
11,
16,
# 26,
13,
17,
17,
11,
18,
13,
18,
16,
16)

coin = 0
pay = 0
pay_rate = 10
for i in lottery_rate:
    pay = i * pay_rate + pay
    coin = pay_rate * i * i + coin
coin = coin / 15
total_get = ((coin-pay) * 15/16)
print("total_pay", pay)
print("total_get",total_get )
print("收益支出比")
print(total_get * 1.0 / pay)

