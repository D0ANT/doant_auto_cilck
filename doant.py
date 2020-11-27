from tkinter import *
from tkinter import messagebox
import pyautogui
import keyboard


window = Tk()
window.title("도개미 오토마우스")
window.geometry("300x100")
window.option_add("*Font", "고딕 20")
ent = Entry(window)
ent.pack()


def click():
    auto_mouse_key = str(ent.get())
    messagebox.showinfo("도개미 오토 클릭 안내", str(ent.get()) + "키를 오토 클릭 하겠습니다.\n중지는 [Ctrl + Shift + C]")
    auto_mouse(auto_mouse_key)

def auto_mouse(auto_key):
    while True:
        pyautogui.press(auto_key)
        try:
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('c'):
                messagebox.showinfo("오토마우스 탈출!", "오토 마우스 탈출!")
                window.destroy()
                break
            else:
                continue
        except:
            break
    
btn = Button(window)
btn.config(text= "enter")
btn.config(width = 5,height = 2)
btn.config(command=click)
btn.pack()

window.mainloop()
