def total_calorie(fruits,fruits_calorie_dic):
    total=0
    for gram in fruits:
        total+=fruits[gram]*fruits_calorie_dic[gram]
    
    return total

def main():
    fruits_calorie_dic={"한라봉": 50/100, "딸기": 34/100, "바나나": 77/100}
    fruits={"딸기": 300, "한라봉": 150}
    print(f"총 섭취 칼로리==>{total_calorie(fruits,fruits_calorie_dic):.2f}")

if __name__=="__main__":
    main()