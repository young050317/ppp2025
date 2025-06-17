import telegram
import asyncio
import PySimpleGUI as sg
import time 
import random


waiting_number = 1
waiting_list = []


def reservation_gui():
    layout = [  [sg.Text("웨이팅 등록 페이지")],
                [sg.Text("이름을 입력해주세요.")],
                [sg.InputText(key = "name")],
                [sg.Text("인원을 입력해주세요 (1~10)")], 
                [sg.InputText(key = "people_num")],
                [sg.Button('등록')], [sg.Button('돌아가기')]  ]
    
    window = sg.Window("young's restaurant", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '돌아가기':
            window.close()
            return None, None
        elif event == '등록':
            name =values["name"].strip()
            try: 
                people_num = int(values["people_num"])
                if people_num <= 0:
                    sg.popup("0보다 큰 수를 입력해주세요.")
                elif people_num > 10:
                    sg.popup("최대 인원은 10명입니다.")
                else:
                    window.close()
                    return people_num, name
            except ValueError:
                sg.popup("숫자만 입력해주세요.")


async def send_message(token, chat_id, name, people_num, waiting_num):
    message = ( f"안녕하세요 {name}고객님!\n"
                f"영스 레스토랑[전주점]에 웨이팅이 성공적으로 등록되었습니다\n"
                f"일시:{time.strftime('%Y.%m.%d %H시 %M분')}\n"
                f"인원: {people_num}명 \n"
                f"대기 번호: {waiting_num}번" )
    bot = telegram.Bot(token=token)
    await bot.send_message(chat_id,message)


def check_waiting_list():
    if not waiting_list:
        return
    
    lines = []
    i = 1
    for waiting in waiting_list:
        name, people, num = waiting
        lines.append(f"{i}. {name} {people}명 {num}번")
        i  += 1

    text = ""
    for line in lines:
        text += line + "\n"

    sg.popup("현재 웨이팅 리스트", text)


def main():
    while True:
        people_num, name = reservation_gui()
        if name is None:
            break

        waiting_num = random.randint(1, 100)
        waiting_list.append((name, people_num, waiting_num))

        token = "7660166562:AAEkqWN8ISso6GOclcGhlYf_wA52vqtHra4" 
        chat_id = 
        asyncio.run(send_message(token, chat_id, name, people_num, waiting_num))
        
        sg.popup(f"{name}님! {people_num}명 웨이팅 등록 완료!! {waiting_num}번")
        
        check_waiting_list()
  

if __name__ == "__main__":
    main()
