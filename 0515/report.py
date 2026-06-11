 중간점검1

 1. 리스트는 시퀀스에 속하는가? 
속함
 2. 시퀀스의 특징에는 어떤것이 있는가?
순서가 있다, 인덱싱 가능, 슬라이싱이 가능, 반복 가능

 중간점검2

 1. 리스트와 튜플의 다른 점은 무엇인가? 
리스트는 변경이 가능, 튜플은 변경이 불가능
 2. 리스트를 튜플로 바꾸려면 어떤 함수를 사용해야 하는가? 
tuple() 함수를 사용해야 함
 3. 패킹과 언패킹을 설명
여러 값을 하나로 묶거나, 반대로 하나에 들어있는 값을 꺼내는 기능
 4. enumerate() 함수는 무엇을 하는 함수인가? 
반복문에서 인덱스와 값을 동시에 얻을 수 있게 해주는 함수

 중간점검3

 1. 리스트와 세트의 차이점은 무엇인가? 
리스트는 순서가 있고 중복이 혀용되지만, 세트는 순서가 없고 중복이 허용되지 않는다.
 2. 세트에 저장된 항목에 접근할 때 인덱스를 사용할 수 있는가? 
사용 불가능
 3. 세트 A와 세트 B의 교집합을 계산하는 수식을 만들어 보자. 
A & B
 4. 세트에 항목을 추가하는 함수는? 
add() 함수

 문자열의 공통 문자

s1=input("첫 번째 문자열:")
s2=input("두 번째 문자열:")

list1 = list( set(s1) & set(s2) ) # 세트로 만들고 교집합 연산을 한다.

print("\n공통적인 글자:", end=" ")
for i in list1:
    print(i, end=" ")
  
  문자열의 공통 문자

txt = input("입력 텍스트: ")
words = txt.split(" ")
unique = set(words)    # 집합으로 만들면 자동적으로 중복을 제거한다.

print("사용된 단어의 개수= ", len(unique))
print(unique)

 중간점검4

 1. 공백 딕셔너리를 생성하는 명령문을 만들어 보자.
dict() 함수를 사용
 2. 딕셔너리에 존재하는 모든 키(key)를 방문하는 코드를 작성해보자. 
for key in dict: print(key)
 3. 딕셔너리 d에 (k,v)를 저장하는 명령문을 만들어보자. 
d[k] = v

 영한 사전

english_dict ={}           # 공백 딕셔너리를 생성한다.

english_dict["one"]="하나" # 딕셔너리에 단어와 의미를 추가한다.
english_dict["two"]="둘'"
english_dict["three"]="셋"

word =input("단어를 입력하시오: ");
print (english_dict[word])

학생 성적 처리

def main():
    address_book ={}                      # 공백 딕셔너리를 생성한다.
    while True :
        user = display_menu();
        if user ==1 :
            name, number = get_contact()
            address_book[name]= number    # name과 number를 추가한다.
        elif user ==2 :                     
            name, number = get_contact()
            address_book.pop(name)        # name을 키로 가지고 항목을 삭제한다.
        elif user ==3 :
            pass                          # 도전 문제 참조
        elif user ==4 :
            for key in sorted(address_book):
                print(key,"의 전화번호:", address_book[key])
        else:
            break
def get_contact():
    name =input("이름: ")
    number =input("전화번호:")
    return name, number

def display_menu() :
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select
main()

 학생 성적 처리

score_dic = {
"Kim":[99,83,95],
"Lee":[68,45,78],
"Choi":[25,56,69]
}

for name, scores in score_dic.items():
    print(name,"의 평균성적=",sum(scores)/len(scores))

 단어 카운터 만들기

from collections import Counter
text_data ="Create the highest, grandest vision possible for your life, because you become what you believe."

a = Counter(text_data.split())

print(a)

 5

 1. 문자열에 포함된 글자들의 코드값을 읽을려면 어떤 함수를 호출해야 하는가? 
oed() 함수를 사용
 2. 문자열의 맨 끝에 있는 글자를 추출하는 명령어를 작성하여보자. 
s[-1] 을 사용
 3. 문자열 A와 문자열 B의 순서를 바교하려면 어떤 명령어를 사용해야 하는가? 
A < B 를 사용

회문 검사

s = input("문자열을 입력하시오:")

s1 = s[::-1] # 문자열을 뒤집는다.

if(s == s1):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")  
  
 머리 글자어 만들기

phrase = input("문자열을 입력하시오: ")

acronym = ""

for word in phrase.upper().split():
    acronym += word[0]

print(acronym)

  이메일 주소 분석

address = input("이메일 주소를 입력하시오.")
(id, domain) = address.split("@") # @를 기준으로 문자열을 나눈다.

print(address)
print("아이디"+id)
print("도메인"+domain)

 lab : 문자열 분석

sentence = input("문자열을 입력하시오: ")

table ={"alphas":0, "digits":0, "spaces":0}

for i in sentence:
    if i.isalpha():
        table["alphas"] += 1
    if i.isdigit():
        table["digits"] += 1
    if i.isspace():
        table["spaces"] += 1

print(table)

  트위터 메시지 처리

t = "Python is very easy and powerful"

length = len(t.split(" "))
print(length)

  OTP 발생 프로그램

import random

s = "0123456789"

passlen = 4 

p = "".join(random.sample(s, passlen))
print(p)
