def average(nums):
    average=sum(nums)/len(nums)
    return average

def main():
    nums=[1,3,5,7,9,11]
    print(f"평균은 {average(nums)}입니다.")

if __name__=="__main__":
    main()