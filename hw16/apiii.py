import os
import requests
from sfarm_hw import submit_to_api


def weather_file(city, year):
    filename = f"weather_{city}_{year}.csv"
    url = f"https://api.taegon.kr/stations/{city}/?sy={year}&ey={year}&format=csv"
    if not os.path.exists(filename):
        resp = requests.get(url)
        resp.encoding = "UTF-8"
        with open (filename, "w", encoding= "UTF-8") as f:
            f.write(resp.text)


def get_weather_data(fname, col_idx):
    weather_data = []
    with open(fname, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            if tokens[col_idx] != "":
                weather_data.append(float(tokens[col_idx]))
    return weather_data


def get_tmax_tmin_diff(fname, tmax_idx, tmin_idx):
    diffs = []
    with open(fname, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            if tokens[tmax_idx] != "" and tokens[tmin_idx] != "":
                diffs.append(float(tokens[tmax_idx]) - float(tokens[tmin_idx]))
    return diffs

def my_abs(x):
    if x < 0:
        return -x
    else:
        return x
    


def main():
    name = "최인영"
    affiliation = "스마트팜학과"
    student_id = "202410120"
    

    weather_file("146", "2015")
    weather_file("146", "2022")
    weather_file("146", "2024")
    weather_file("119", "2024")

    tmax = 3
    tmin = 5
    tavg = 4
    rain = 9
    rain_2015 = sum(get_weather_data("weather_146_2015.csv", rain))
    tavg_2022 = get_weather_data("weather_146_2022.csv", tavg)
    diffs_2024 = get_tmax_tmin_diff("weather_146_2024.csv", tmax, tmin)
    rain_119_2024 = sum(get_weather_data("weather_119_2024.csv", rain))
    rain_146_2024 = sum(get_weather_data("weather_146_2024.csv", rain))

    answer1 = f"{rain_2015:.1f}"
    answer2 = f"{max(tavg_2022):.1f}"
    answer3 = f"{max(diffs_2024):.1f}"
    answer4 = f"{my_abs(rain_119_2024 - rain_146_2024):.1f}"

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)


if __name__ == "__main__":
    main()


