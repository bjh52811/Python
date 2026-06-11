 사실 판별

num = int(input("Enter a number: "))

fact = 1

print(num, end="! = ")
for i in range(num, 0, -1):
    fact *= i
    if i > 1:
        print(i, end=" * ")
    else :
        print(i, end=" = ")

print(fact


    for 예제

for i in [1, 5, 3, 2, 4]:
    print("방문을 환영합니다.", i

    윤년 판별
          
  year =  int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else :
    print(year, "is a common year.")

  배송비 판정

price = int(input("상품의 가격: "))
if price > 20000 :
    shipping_cost = 0
else :
    shipping_cost = 3000
print("배송비: ", shipping_cost)
