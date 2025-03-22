import math

r=int(input("반지름을 입력하시오.==>"))

circumference=2*math.pi*r
area=math.pi*pow(r,2)

print(f"원의 둘레는 {circumference:.1f}입니다.")
print(f"원의 넓이는 {area:.2f}입니다.")