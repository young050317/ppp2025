def text2list(txt):
    txt_list=txt.split()
    nums=[int(x) for x in txt_list]    
    return nums

def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    sorted_list=sorted(nums)
    return sorted_list[len(sorted_list)//2] 

def read_text(filename):
    text=""
    with open(filename) as f:
        lines=f.readlines()
        for line in lines:
            print(f"!{line.strip()}!")
            text+=" "+line.strip()
    return text

def main():
    text=read_text("C:/code/ppp2025/hw08/numbers2.txt")
    nums=text2list(text)
    print("숫자는 총 {}개".format(len(nums)))
    print("평균값은 {:.1f}".format(average(nums)))
    print("최댓값은 {}".format(max(nums)))
    print("최솟값은 {}".format(min(nums)))
    print("중앙값은 {}".format(median(nums)))

if __name__=="__main__":
    main()