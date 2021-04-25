import threading
from tkinter import *
import webbrowser
import time


def wd(mem):

    def run():
        link = entry_label.get()
        mem.append(link)

    root = Tk()
    title_label = Label(root, text="Mini Broswer", pady=10, padx=50)
    run_button = Button(root, text="Run", padx=10,  command=run)
    entry_label = Entry(root, text="Digite a URL do site que quer abrir", width=100)

    title_label.grid(row=0, column=0)
    run_button.grid(row=1, column=1)
    entry_label.grid(row=1, column=0)

    root.mainloop()


def render(mem):
    mem_old = mem[-1]
    while True:
        if mem[-1] == mem_old:
            print("Esperando URL...")
        else:
            print(f'render( {mem[-1]} )')
            webbrowser.open_new_tab(mem[-1])
            mem_old = mem[-1]
            break
        time.sleep(1)


memoria = ["nada"]


t1 = threading.Thread(target=wd, kwargs=dict(mem=memoria))
t2 = threading.Thread(target=render, kwargs=dict(mem=memoria))

t1.start()
t2.start()
