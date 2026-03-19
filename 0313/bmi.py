weight = float(input("몸무게를 입력하세요 (kg): "))
height = float(input("키를 입력하세요 (cm): "))
bmi = (weight / ((height / 100) ** 2))  # Convert cm to m
print("당신의 BMI=", bmi)