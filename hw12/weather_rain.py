import os
import requests



def download_weather():
    filename = "weather_146_2020.csv"
    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    if not os.path.exists(filename):    
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(resp.text)



def average(nums):
    return sum(nums)/len(nums)



def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas



def main():
    filename="weather_146_2020.csv"
    result_filename = "weather_2020_result.txt"

    download_weather()

    tavgs = get_weather_data(filename, 4)
    avg_temp = average(tavgs)

    rainfalls = get_weather_data(filename, 9)
    count_over5_rain = len([x for x in rainfalls if x >= 5])
    total_rain = sum(rainfalls)

    
    with open(result_filename, "w", encoding="utf-8") as f:
        f.write(f"1. 연평균 기온(avg. of 일평균) = {avg_temp:.2f}도\n")
        f.write(f"2. 5mm이상 강우일수 = {count_over5_rain}일\n")
        f.write(f"3. 총 강수량은 = {total_rain:,.1f}mm\n")




if __name__ == "__main__":
    main()