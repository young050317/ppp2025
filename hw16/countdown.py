import time


def count_down(count):
    for n in range(count):
        print(f"{count - n}...", end="\r")
        #print(f"{count - n}...", end="")
        time.sleep(1)
    print("땡")


def main():
    count_down(5)


if __name__ == "__main__":
    main()