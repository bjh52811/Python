 성적처리 프로그램

STUDENT = 5
lst = []
count = 0

for i in range(STUDENT):
    value = int(input("성적을 입력하시오."))
    lst.append(value)

print("\n성적 평균=", sum(lst) / len(lst))
print("최대점수=", max(lst))
print("최소점수=", min(lst))
for score in lst:
    if score >= 80:
        count += 1
print("80점 이상=", count)

 리스트에서 2번째로 큰 수 찾기

list1 = [1, 2, 3, 4, 15, 99]
list1.sort()
print("두 번째로 큰 수=", list1[-2])
list1 = [1, 2, 3, 4, 15, 99]
list1.remove(max(list1)) 
print("두 번째로 큰 수=", max(list1)) 

  컨테스트 콘평가

scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
print("제거전", scores)
scores.remove(max(scores))
scores.remove(min(scores))
print("제거후", scores)

 리스트로 스택 흉내내기

stack = []
for i in range(3) :
    f = input("과일을 입력하시오: ")
stack.append(f)
for i in range(3) :
    print( stack.pop() )

 친구관리 프로그램

menu = 0
friends = []
while menu != 9:
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1:
        print(friends)
    elif menu == 2:
        name = input("이름을 입력하시오: ")
        friends.append(name)
    elif menu == 3:
        del_name = input("삭제하고 싶은 이름을 입력하시오: ")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("이름이 발견되지 않았음")



중간 점검
1. 함수란? 
특정 목적을 수행하기 위해 독립적으로 설계된 코드의 집합
2. 함수를 사용하는 이유는 무엇인가? 
코드의 재사용성, 가독성 향상, 유지보수 용이성

예제
def get_area(radius):
    area = 3.14*radius**2
    return area
result = get_area(3)
print("반지름이 3인 원의 면적=", result)

 리스트 슬라이싱

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
reversed = numbers[::-2]
print(reversed)

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
numbers[1:] = [ ]
print(numbers)

리스트 변경 함수

salaries = [200, 250, 300, 280, 500]

def modify(values, factor) :
    for i in range(len(values)) :
        values[i] = values[i] * factor

print("인상전", salaries)
modify(salaries, 1.3)
print("인상후", salaries)

리스트 함축 사용하기

numbers = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
print(numbers)

 누적값 리스트 만들기

list1=[10, 20, 30, 40, 50]
list2=[sum(list1[0:x+1]) for x in range(0, len(list1))]
print("원래 리스트: ",list1)
print("새로운 리스트: ",list2)

 피타고라스 삼각형

[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if
x**2 + y**2 == z**2]

new_list = []
for x in range(1, 30):
    for y in range(x, 30):
        for z in range(y, 30):
            if x**2+y**2==z**2:
                new_list.append((x, y, z))
print(new_list)
