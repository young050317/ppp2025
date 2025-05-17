def str2float(default_value: float = -999) -> list:
    num = []
    while True:
        try:
            x = input("X = ? ")

            if x == "-1":
                break

            
            if float(x) % 1 == 0 and float(x) > 0:
                num.append(int(x))
            else:
                continue
            
        except ValueError:
            continue
            
        
    return num
    

def average(num: list):
    return sum(num) / len(num)


def main():
    value = str2float()
    print(f"입력된 값은 {value}입니다. 총 {len(value)}개의 자연수가 입력되었고, 평균은 {average(value)}입니다.")


if __name__ == "__main__":
    main()

