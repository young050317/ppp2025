import math

print("각      라디안      sin      cos      tan")
print("-"*44)


for i in range(11):
    print(f"{i}º      {i*math.pi/180:.4f}    {math.sin(i * math.pi / 180):.4f}    {math.cos(i * math.pi / 180):.4f}   {math.tan(i * math.pi / 180):.4f}")