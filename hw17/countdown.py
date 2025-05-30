import time
import tkinter as tk
from tkinter import simpledialog
from rich import print

window = tk.Tk()
window.withdraw()


def gui_input(text: str) -> str:
    return simpledialog.askstring(title="입력창", prompt=text)


def count_down(count):
    for n in range(count):
        print(f"[blue]{count - n}...[/blue]", end="\r")
        time.sleep(1)
    print("[red]땡[/red]")


def main():
    s = gui_input("몇 초 카운트할까요~?")
    count_s = int(s)
    count_down(count_s)



if __name__ == "__main__":
    main()