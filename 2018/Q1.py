# 2018 BIO Q1

interest, repay = map(float, input().split())
debt = 100
repaid = 0
while debt:
    debt += debt*interest/100
    if max(50, debt*(repay/100)) < debt:
        repaid += max(50, debt*(repay/100))
        debt -= max(50, debt*(repay/100))
    else:
        repaid += debt
        debt = 0
        break
print(round(repaid,2))
