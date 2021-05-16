from tkinter import *
from tkinter import messagebox
import pyautogui
import keyboard
import sys


window = Tk()
window.title("도개미 오토마우스")
window.geometry("300x125")
window.option_add("*Font", "고딕 20")
ent = Entry(window)
ent.pack()

at = 'false'

def click():
    global at
    auto_mouse_key = str(ent.get())
    if auto_mouse_key != "right click" and auto_mouse_key != "우클릭" and auto_mouse_key != "left click" and auto_mouse_key != "좌클릭" and auto_mouse_key != "shift" and auto_mouse_key != "ctrl" and auto_mouse_key != "alt" and auto_mouse_key != "tab" and auto_mouse_key != "esc" and auto_mouse_key != "doant":
        messagebox.showwarning("도개미 오토 클릭 경고","제대로 된 키를 입력하세요")
    elif auto_mouse_key == "doant":
        window.title("도개미 슈퍼 오토클릭")
        ent.delete(0,len(ent.get()))
        ent.insert(0,"도개미 짱")
        messagebox.showinfo("도개미 슈퍼오토클릭 안내", "제작자는 도개미입니다.")
    else:
        messagebox.showinfo("도개미 오토 클릭 안내", str(ent.get()) + "키를 오토 클릭 하겠습니다.\n중지는 [Ctrl + Shift + C] 또는 stop버튼")
        at = 'true'
        auto_mouse(auto_mouse_key)

def auto_mouse(auto_key):
    at = 'true'
    if auto_key == "left click" or auto_key == "좌클릭":
        while True:
            pyautogui.click(button='left')
            try:
                if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('c'):
                    loopbreak()
                else:
                    continue
            except:
                sys.exit()
                break
    if auto_key == "right_click" or auto_key == "우클릭":
        while True:
            pyautogui.click(button='right')
            try:
                if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('c'):
                    loopbreak()
                else:
                    continue
            except:
                break
    while True:
        pyautogui.press(auto_key)
        pyautogui.press(auto_key)
        pyautogui.press(auto_key)
        pyautogui.press(auto_key)
        pyautogui.press(auto_key)
        pyautogui.press(auto_key)
        pyautogui.press(auto_key)
        pyautogui.press(auto_key)
        pyautogui.press(auto_key)
        try:
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('c'):
                loopbreak()
            else:
                continue
        except:
            break
def loopbreak():
    global at
    if at == 'true':
        messagebox.showinfo("오토 마우스 탈출!", "오토 마우스 탈출!")
        at='false'
        sys.exit()
        window.destroy()
    else:
        messagebox.showwarning("도개미 오토클릭 에러", "오토클릭 시작은 하셔야죠")
    
btn = Button(window)
btn.config(text= "enter")
btn.config(width = 6,height = 1)
btn.config(command=click)
btn.pack()

btn1 = Button(window)
btn1.config(text = "stop")
btn1.config(width = 6,height = 1)
btn1.config(command=loopbreak)
btn1.pack()

window.mainloop()
