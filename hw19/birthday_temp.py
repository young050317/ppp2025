import requests
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/statons/{station_id}/?sy={year}&format=csv"
    with open (filename, "w", encoding = "UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)


def main():
    start_y = 2005
    end_y = 2025
    years = []
    tmaxs = []

    for year in range(start_y, end_y + 1):
        filename = f"weather_{year}.csv"
        download_weather(146, year,filename)
        df = pd.read_csv(filename, skipinitialspace=True)

        for i in range(len(df)):
            if df["month"][i] == 3 and df["day"][i] == 17:
                value = df["tmax"][i]
                tmaxs.append(value)
                years.append(year)
    

    
    fig, ax = plt.subplots()
    ax.plot(years, tmaxs, marker='o')
    ax.set_ylim([0,30])
    
    ax.set_xlabel("연도")
    ax.set_ylabel("온도")
    plt.show()
    plt.savefig("Line_gragh_birth.png")


if __name__ == "__main__":
    main()