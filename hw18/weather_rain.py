import requests
import pandas as pd
from sfarm_hw import submit_to_api


def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/statons/{station_id}/?sy={year}&format=csv"
    with open (filename, "w", encoding = "UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)


def main(): 
    name = "최인영"
    affiliation = "스마트팜학과"
    student_id = "202410120"

    #연강수량
    filename = "weather_146_2012.csv"
    download_weather(146, 2012, "weather_146_2012.csv")
    df = pd.read_csv(filename, skipinitialspace=True)
    answer1 = f"{df["rainfall"].sum():.1f}"


    #최대기온
    filename = "weather_146_2024.csv"
    download_weather(146, 2024, "weather_146_2024.csv")
    df = pd.read_csv(filename, skipinitialspace=True)
    answer2 = f"{df["tmax"].max():.1f}"


    #최대일교차
    filename = "weather_146_2020.csv"
    download_weather(146, 2020, "weather_146_2020.csv")
    df = pd.read_csv(filename, skipinitialspace=True)
    df["tdiff"] = df["tmax"] - df["tmin"]
    answer3 = f"{df["tdiff"].max():.1f}"

    filename_119 = "weather_119_2019.csv"
    filename_146 = "weather_146_2019.csv"
    download_weather(119, 2019, "weather_119_2019.csv")
    download_weather(146, 2019, "weather_146_2019.csv")
    df1 = pd.read_csv(filename_119, skipinitialspace=True)
    df2 = pd.read_csv(filename_146, skipinitialspace=True)

    rain_119 = df1["rainfall"].sum()
    rain_146 = df2["rainfall"].sum()

    if rain_119 > rain_146:
        rdiff = rain_119 - rain_146
    else :
        rdiff = rain_146 - rain_119

    answer4 = f"{rdiff:1f}"

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)



if __name__ == "__main__":
    main()