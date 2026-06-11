 원주율 계산기

def msg():
    print("hello world")
    print("welcome to python world")
    print("THis is a test message")


def emp():
    pass
def msg2(rep):
    for i in range(rep):
        print("this is a repeated message")

def getArea(radius):
    area = 3.14 * radius * radius
    return area
        
emp()
msg()
msg2(3)
area = getArea(5)
print("this of the circle with radius 5 is", area)


 넓이 구하기

def rectangleArea(w, h):
    area = w * h
    return area

def main():
    width = 4
    height = 5
    area = rectangleArea(width, height)
    print("The area of the rectang is", area)

main()

숫자 맞추기

import random

tries = 0
guess = 0
answer = random.randint(1, 200)

print("1부터 200까지의 숫자중 하나를 적어 맞춰보시오.")

while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < answer:
        print("너무 낮습니다. 다시 시도해보세요.")
    elif guess > answer:
        print("너무 높습니다. 다시 시도해보세요.")

if guess == answer:
    print("축하합니다. 시도 횟수는", tries, "입니다.")
else:
    print("정답은", answer, "입니다.")
