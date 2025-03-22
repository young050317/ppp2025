calories=[50,34,77]

eat_orange=int(input("한라봉을 몇g 섭취했나요?"))
eat_strawberry=int(input("딸기를 몇g 섭취했나요?"))
eat_banana=int(input("바나나를 몇g 섭취했나요?"))

total_calories=calories[0]/100*eat_orange+calories[1]/100*eat_strawberry+calories[2]/100*eat_banana

print("한라봉 {}g, 칼로리={}".format(eat_orange,calories[0]/100*eat_orange))
print("딸기 {}g, 칼로리={}".format(eat_strawberry,calories[1]/100*eat_strawberry))
print("바나나 {}g, 칼로리={}".format(eat_banana,calories[2]/100*eat_banana))
print("총 칼로리는 {}입니다".format(total_calories))