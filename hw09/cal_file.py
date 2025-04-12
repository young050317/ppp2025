def read_db(filename):
    calorie_dic=dict()    
    
    with open(filename,encoding="utf-8-sig") as f:
        lines=f.readlines()
        for line in lines[1:]:
            line=line.strip()
            tokens=line.split(",")
            calorie_dic[tokens[0]]=int(tokens[1])
        
    return calorie_dic


def main():
    fruit_cal=read_db("C:/code/ppp2025/calorie_db.csv")
    fruit_eat={"블루베리": 150, "딸기":200}
    

    total=0
    
    for item in fruit_eat:
        total+=(fruit_cal[item]*fruit_eat[item])

    print(f"총 섭취 칼로리==>{(total/100):.2f}")

if __name__=="__main__":
    main()