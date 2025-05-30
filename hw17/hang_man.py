import random
import tkinter as tk
from tkinter import simpledialog
from rich import print

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="문제", prompt=text)



def check(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i] = solution[i]
            is_correct= True
    return is_correct
         


def main():
    problems =["apple", "banana"]

    solution = problems[random.randrange(len(problems))]
    
    is_correct = False

    lives = 5

    answer = ["_" for n in range(len(solution))]

    while True:
        input_ch = gui_input(f"{''.join(answer)} ?")
        
        if check(solution, answer, input_ch):
            print(f"[blue]{input_ch}[/blue]가 포함되어 있습니다.")
        else:
            lives -= 1

        if "_" not in answer:
            is_correct = True
            break

        if lives < 0:
            break

    if is_correct:
            print("[green]정답입니다![/green]")
    else: 
            print(f"[red]땡. 정답은 {solution}입니다[/red]")

    
if __name__ == "__main__":
    main()