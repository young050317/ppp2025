import random

chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def to_chosung_ch(ch):
    if '가' <= ch <= '힣':
        index = (ord(ch) - ord('가')) // 588
        return chosung_list[index]
    else:
        return ch


def to_chosung(text):
    full_text = []
    for ch in text:
        full_text.append(to_chosung_ch(ch))
    return "".join(full_text)


def main():
    problems =["바나나", "딸기", "토마토", "복숭아"]
    solution = random.choice(problems)
    chosung = to_chosung(solution)

    print(f"초성: {chosung}")

    for i in range(3):
        answer = input("단어를 맞춰보세요: ").strip()
        if answer == solution:
            print("정답!")
            break
        else:
            print("오답!")
    else: 
        print(f"게임 오버. 정답은 {solution}입니다")

    

if __name__ == "__main__":
    main()