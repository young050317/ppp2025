def get_range_list(n):
    num_list=list(range(1,1+n))
    return num_list

def main():
    n=int(input("정수를 입력하시오==>"))
    print("1-n까지 리스트")
    print(get_range_list(n))



if __name__=="__main__":
    main()