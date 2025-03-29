def gugudan(dan):
    for i in range(9):
        i=i+1
        print(f"{dan}*{i}={i*dan}")
        
def main():
    dan=int(input("숫자를 입력하시오.==>"))
    gugudan(dan)
    
if __name__=="__main__":
    main()