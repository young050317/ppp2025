def toggle_text(text: str) -> str:
    result = []
    for ch in text:
        if 97 <= ord(ch) <= 122:
            result.append(chr(ord(ch)-32))
    
        elif 65 <= ord(ch) <= 90:
            result.append(chr(ord(ch)+32))
        else :
            result.append(ch)
    
    return "".join(result)


def caesar_encode_ch(ch, shift):
    if 65 <= ord(ch) <= 90:
        return chr((ord(ch) - 65 + shift) % 26 + 65)
    elif 97 <= ord(ch) <= 122:
        return chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        return ch


def caesar_encode(text: str, shift: int = 3) -> str:
    full_text = []
    for ch in text:
        encoded_ch = caesar_encode_ch(ch, shift)
        full_text.append(encoded_ch)

    return "".join(full_text)
    

def caesar_decode(text: str, shift: int = 3) -> str:
    return caesar_encode(text, -shift)


def main():
    input_text = input("문자열 입력 ==> ")
    print(f"{input_text} => {toggle_text(input_text)}")

    print(f'caesar_encode("{input_text}") == "{caesar_encode(input_text)}"')
    print(f'caesar_decode("{input_text}") == "{caesar_decode(input_text)}"')


if __name__ == "__main__":
    main()