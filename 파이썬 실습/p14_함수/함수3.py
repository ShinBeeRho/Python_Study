customer = input("고객의 등급을 입력해주세요 : ")
pay = int(input("상품의 금액을 입력해주세요 : "))

def discount(customer, pay):
    discountPay = 0
    if customer == 'vip' :
        discountPay = pay * 0.7
    elif customer == 'gold' :
        discountPay = pay * 0.8
    elif customer == 'silver' :
        discountPay = pay * 0.9
    else :
        discountPay = pay * 0.95
        
    return discountPay

discountPay = int(discount(customer, pay))

print(f"{customer} 고객의 할인 적용된 금액은 {discountPay}입니다.")