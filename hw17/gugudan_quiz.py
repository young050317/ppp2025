import random
import tkinter as tk
from tkinter import simpledialog
from rich import print

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="문제", prompt=text)

def problem():
    dan = random.randint(2,9)
    mul = random.randint(1,9)
    
    try:
        ans = int(input(f"{dan} X {mul} = ?  "))
    except ValueError:
        return False

    if ans == dan*mul:
        print("[green]정답~![/green]")
        return True
    else:
        print("[red]땡~![/red]")
        return False


def main():
    score = 0
    total_problem = 5

    for n in range(total_problem):
        
        is_correct = problem()
        if is_correct:
            score += 1
    print(f"총점은 [yellow]{score}, {score / total_problem * 100}점[/yellow]")



if __name__ == "__main__":
    main()