def read_db(filename):
    tavglist=[]
    rainfalllist=[]
       
    with open(filename,encoding="utf-8-sig") as f:
        lines=f.readlines()
        for line in lines[1:]:
            line=line.strip()
            tokens=line.split(",")
            tavg=float(tokens[4])
            rainfall=float(tokens[9])
            tavglist.append(tavg)
            rainfalllist.append(rainfall)

    return tavglist,rainfalllist

def tavg(tavglist):
    return sum(tavglist)/len(tavglist)

def rain_5mm_day(rainfalllist):
    return sum(1 for r in rainfalllist if r >=5)
    
def total_rain(rainfalllist):
    return sum(rainfalllist)
    
def main():
    tavglist,rainfalllist=read_db("C:/code/ppp2025/weather(146)_2022-2022.csv")

    print(f"연 평균 기온은 {tavg(tavglist):.2f}℃입니다.")
    print(f"5mm이상 강수일수는 {rain_5mm_day(rainfalllist)}일입니다.")
    print(f"총 강수량은 {total_rain(rainfalllist):.2f}mm입니다.")


if __name__=="__main__":
    main()