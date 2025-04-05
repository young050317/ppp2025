def average(nums):
    average=sum(nums)/len(nums)
    return average

def main():
    text_input=input("==>")
    print(text_input)
    # print(text_input.split())
    nums=[]
    for text in text_input.split(","):
        nums.append(int(text))
    print(f"평균은 {average(nums)}입니다.")

if __name__=="__main__":
    main()