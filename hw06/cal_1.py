
def main():
    fruit_cal={"한라봉":50/100,"딸기":34/100,"바나나":77/100}
    
    total=0

    for item in fruit_cal:
        eat_fruit=int(input("{} 몇 g을 먹었나요?==>".format(item)))
        eat_cal=eat_fruit*fruit_cal[item]
        total=total+eat_cal
    
    print(f"총 섭취 칼로리==>{total:.2f}")

if __name__=="__main__":
    main()


