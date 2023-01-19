from tkinter import *
import tkinter as tk
from tkinter import ttk
import googletrans
from googletrans import Translator


def label_change():
    src=src_lang.get()
    dest=dest_lang.get()
    src_label.configure(text=src)
    dest_label.configure(text=dest)
    root.after(100, label_change)


def translate():
    text=text1.get(1.0, END)
    t1=Translator()
    trans_text=t1.translate(text, src=src_lang.get(), dest=dest_lang.get())
    trans_text=trans_text.text
    text2.delete(1.0, END)
    text2.insert(END, trans_text)

def switch_lang():
    src = src_lang.get()
    dest = dest_lang.get()
    src_lang.set(dest)
    dest_lang.set(src)
    src_label.config(text=dest)
    dest_label.config(text=src)
    

def close():  
    root.destroy()  


root = tk.Tk()
root.geometry('550x780')
root.resizable(0,0)
root.title("Google Translate by RNP")
root.config(bg = 'gray12')

languange = googletrans.LANGUAGES
languangeV = list(languange.values())
lang1=languange.keys()

# JUDUL/TITLE
Judul = Label(root, text='GOOGLE TRANSLATE BY RNP', 
                    font='candara 20 bold',
                    bg='gold', 
                    fg='black', 
                    width=31,
                    height=1,
                    bd=3,
                    relief='sunken')
Judul.pack(pady=20, ipadx=20, ipady=15)

# BAHASA ASAL
src_lang = ttk.Combobox(root, values=languangeV, 
                                font="Roboto 13", 
                                state="r")
src_lang.place(relx=0.22, y=120, anchor=N)
src_lang.set("Indonesian")

# BAHASA TUJUAN
dest_lang = ttk.Combobox(root, values=languangeV, 
                                font="Roboto 13", 
                                state="r")
dest_lang.place(relx=0.78, y=120, anchor=N)
dest_lang.set("English")


# LABEL BAHASA ASAL
src_label = tk.Label(root, text="Indonesian", 
                            font='Roboto 15', 
                            bg='DeepSkyBlue', 
                            fg='black', 
                            width=18, 
                            height=2, 
                            bd=3, 
                            relief='sunken')
src_label.place(relx=0.22, y=160, anchor=N)

# LABEL BAHASA TUJUAN
dest_label = tk.Label(root, text="English", 
                            font='Roboto 15', 
                            bg='DeepSkyBlue', 
                            fg='black', 
                            width=18, 
                            height=2, 
                            bd=3, 
                            relief='sunken')
dest_label.place(relx=0.78, y=160, anchor=N)


# TOMBOL ARROW UNTUK MENUKAR BAHASA
arrow = tk.Button(root, text=" ⇄ ", 
                        font="Roboto 35", 
                        bg='DeepSkyBlue', 
                        width=2, 
                        height=0, 
                        bd=3, 
                        relief='sunken', 
                        command=switch_lang)
arrow.place(relx=0.5, y=120, anchor=N)


# KOLOM INPUT
frame_input=Frame(root, bg="Black", bd=0, relief=SOLID)
frame_input.place(relx=0.50, y=230, anchor=N ,width=520,height=180)

text1=Text(frame_input, font="Roboto 14", 
                        bg="azure", 
                        fg="black", 
                        bd=1, 
                        relief=SOLID, 
                        wrap=WORD)
text1.place(relx=0, rely=0, width=510,height=179)

scrollbar1=Scrollbar(frame_input)
scrollbar1.pack(side="right",fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# KOLOM OUTPUT
frame_output=Frame(root, bg="Black", bd=0, relief=SOLID)
frame_output.place(relx=0.50, y=485, anchor=N ,width=520,height=180)

text2=Text(frame_output, font="Roboto 14", 
                            bg="azure", 
                            fg="black", 
                            bd=1, 
                            relief=SOLID, 
                            wrap=WORD)
text2.place(relx=0, rely=0, width=510,height=179)

scrollbar2=Scrollbar(frame_output)
scrollbar2.pack(side="right",fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


# TOMBOL TRANSLATE
translate_btn = tk.Button(root, 
                    text="TRANSLATE",
                    font='candara 14 bold',
                    activebackground="white",
                    cursor="hand2",
                    bd=3,
                    relief='sunken',
                    width=51,
                    height=1,
                    bg="green1",
                    fg="black",
                    command=translate)
translate_btn.place(relx=0.50, y=425, anchor=N)


# TOMBOL EXIT
exit = Button(root,
                    text="EXIT",
                    font='candara 14 bold',
                    activebackground="white",
                    cursor="hand2",
                    bd=3,
                    relief='sunken',
                    width=51,
                    height=1,
                    bg="darkorange2",
                    fg="black",
                    command=close)
exit.place(relx=0.50, y=680, anchor=N)

label_change()
root.mainloop()
