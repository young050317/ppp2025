import math

weight=int(input("몸무게를 입력하시오.==>"))
height=int(input("키를 입력하시오.==>"))

height_m=height/100

bmi=weight/math.pow(height_m,2)

print("몸무게={},키={}일 떄, bmi={}".format(weight,height,bmi))

if 23<=bmi<=24.9:
    print("비만 전단계입니다.")
elif 25<=bmi<=29.9:
    print("1단계 비만입니다.")
elif 30<=bmi<=34.9:
    print("2단계 비만입니다.")
elif bmi>=35:
    print("3단계 비만입니다.")
else :
    print("정상입니다.")