def c2f(t_c):
    return (t_c*1.8)+32

def main():
    t_c=int(input("섭씨 온도를 입력하시오.==>"))
    temp_f=c2f(t_c)

    print(f"{t_c}C=>{temp_f}F")

if __name__ == "__main__":
    main()