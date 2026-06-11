 1. 함수란 무엇인가?
목적을 수행하기 위해 독립적으로 설계된 코드의 집합
 2. 함수를 사용하는 이유는 무엇인가?
코드의 재사용성, 가독성 향상, 유지보수 



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
