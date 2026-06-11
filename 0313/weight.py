weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 cm 단위로 입력하시오: "))
height_m = height / 100  # cm를 m로 변환
bmi = (weight / (height_m ** 2))
print("당신의 BMI=", bmi)
