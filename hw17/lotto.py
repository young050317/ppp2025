import random
import tkinter as tk
from tkinter import simpledialog
from rich import print

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="문제", prompt=text)


def get_lotto():
    lotto_list = []
    while True:
        n = random.randint(1, 45)
        if n not in lotto_list:
            lotto_list.append(n)
        if len(lotto_list) == 6:
            break
   
    return sorted(lotto_list)


def main():
    list_num = int(gui_input("이번엔 몇 천원을 쓸 거죠?"))
    print(f"[yellow]이번주 행운번호[/yellow]")
    for i in range(list_num):
        lotto_num = get_lotto()
        print(f"[red]{lotto_num}[/red]")
    print(f"[green]!Good Luck![/green]")


if __name__ == "__main__":
    main()