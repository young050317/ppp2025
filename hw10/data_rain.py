def average(nums):
    return sum(nums)/len(nums)



def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas



def get_weather_data_int(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(int(tokens[col_idx]))

    return weather_datas



def count_bigger_days(nums,criteria):
    basket=[]
    for num in nums:
        if num>= criteria:
            basket.append(num)
        return len(basket)



def get_rain_events(rainfalls):
    events = []
    c_days = 0
    for rain in rainfalls:
        if rain > 0:
            c_days += 1
        else:
            if c_days > 0:
                events.append(c_days)
            c_days = 0
    if c_days > 0:
        events.append(c_days)
        print(events)

    return events



def rain_events(rainfalls):
    sum=[]
    c_days_amount=0
    for rain in rainfalls:
        if rain > 0:
            c_days_amount += rain

        else:
            if c_days_amount > 0:
                sum.append(c_days_amount)
                c_days_amount = 0
    if c_days_amount > 0:
        sum.append(c_days_amount)
    return sum


def sumifs(rainfalls, months, selected=[6,7,8]):
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected:
            total += rain

    return total



def main():
    filename="C:/ppp2025/weather(146)_2022-2022.csv"

    #1. 일평균 기온의 연평균
    tavgs = get_weather_data(filename, 4)
    print(f"1. 연평균 기온(avg. of 일평균) = {average(tavgs):.2f}도")


    #2.5mm이상인 강우일수
    rainfalls=get_weather_data(filename, 9)
    # count_over5_rain=count_bigger_days(rainfalls,5)
    count_over5_rain = len([x for x in rainfalls if x >= 5])
    print(f"2. 5mm이상 강우일수 = {count_over5_rain}일")


    #3. 총 강수량은
    print(f"3. 총 강수량은 = {sum(rainfalls):,.1f}mm")


    #4. 최장연속강우일수
    print(f"4. 최장연속강우일수 = {max(get_rain_events(rainfalls))}일")


    #5. 강우이벤트 중 최대 강수량은

    rainfalls = get_weather_data(filename, 9)
    event_sum = rain_events(rainfalls)
    c_day_max = max(event_sum)
    print(f"5. 강우이벤트 중 최대 강수량은 {c_day_max:.2f}mm입니다.")


    #6. 가장 더운날 top3
    top3_tmax = sorted(get_weather_data(filename, 3), reverse=True)[:3]
    # top3_tmax = sorted(get_weather_data(filename, 3))[-3:][::-1]
    print(f"6. 가장 더운날 top3는 {top3_tmax}입니다.")

    
    #여름철 강수량
    months = get_weather_data_int(filename, 1)
    print(f"여름철 강수량은 {sumifs(rainfalls, months, selected=[6,7,8]):.1f}입니다.")


    #2021년과 2022년 총 강수량을 구하시오.
    filename_20yr="C:/ppp2025/weather(146)_2001-2022.csv"
    years=get_weather_data_int(filename_20yr,0)
    rainfalls=get_weather_data(filename_20yr,9)
    print(f"2021년 총 강수량은 {sumifs(rainfalls, years, selected=[2021]):.1f}")
    print(f"2022년 총 강수량은 {sumifs(rainfalls, years, selected=[2022]):.1f}")



if __name__ == "__main__":
    main()