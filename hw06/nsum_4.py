def sum_n(n):
    total=0
    for i in range(n):
        n=i+1
        total=total+n
    return total
   
def main():
    n=int(input("숫자를 입력하시오==>"))
    print("1부터 {}까지의 합==>{}".format(n,sum_n(n)))

if __name__=="__main__":
    main()
