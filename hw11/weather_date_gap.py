def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas



def get_weather_date(fname):
    weather_dates = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]),int(tokens[1]),int(tokens[2])])
    
    return weather_dates



def maximum_temp_gap(dates, tmax, tmin):
    year_gap = []

    for year in range(2001, 2023):
        max_gap = 0
        max_gap_date = []

        for i in range(len(dates)):
            year_of_data, month, day = dates[i]
            if year_of_data == year:
                tx = tmax[i]
                tm = tmin[i]
                gap = tx - tm

                if max_gap < gap:
                    max_gap = gap
                    max_gap_date = [year_of_data, month, day]
            
        if max_gap_date:
            year_gap.append([max_gap_date, max_gap])

    return year_gap

        


    
def main():
    filename = "C:/ppp2025/weather(146)_2001-2022.csv"
    dates = get_weather_date(filename)
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)

    year_max_gaps = maximum_temp_gap(dates, tmax, tmin)

    for date, gap in year_max_gaps:
        print(f"{date[0]}/{date[1]:02d}/{date[2]:02d}  {gap:.1f}")



if __name__ == "__main__":
    main()