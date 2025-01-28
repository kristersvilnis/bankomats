from tkinter import *
from tkinter import font
from tkinter import messagebox

platums = 1280
garums = 960
root = Tk()
root.title("test")

Catamaran = font.Font(family="Catamaran-Bold", size=80, weight="bold")

canvas = Canvas(root, width=platums, height=garums, bg="#574964")
canvas.pack()

pin_var=StringVar()

vid_x = platums / 2
vid_y = garums / 2

def meklet_pin():
    try:
        with open("pareizais_kods.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "PIN file not found!")
        return None

def apstiprinat_pin():
    uzglabatais_pin = meklet_pin()
    ievaditais_pin = pin_var.get()

    if uzglabatais_pin is None:
        return
    
    if ievaditais_pin == uzglabatais_pin:
        darijuma_ekrans()
    else:
        messagebox.showerror("Error", "Ievadītais PIN kods ir nepareizs! Mēģini vēlreiz.")

def on_rectangle_click(event):
    print("Rectangle clicked!")

def darijuma_ekrans():
    canvas.destroy()
    
    canvas_darijums = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas_darijums.pack()

    noradit_darijumu = canvas_darijums.create_text(vid_x, 140, \
                                      text="Lūdzu, norādiet darījumu!", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    noradit_darijumu_eng = canvas_darijums.create_text(vid_x, 210, \
                                      text="Please select an option!", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    naudas_iznemsana = canvas_darijums.create_rectangle(0, vid_y-35, 500, vid_y+35,
                                                         outline="#786689", fill = "#786689",
                                                         width = 10)
    naudas_iznemsana_teksts = canvas_darijums.create_text(250, vid_y, \
                                                         text="Naudas izņemšana", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                         anchor="center")
    canvas_darijums.tag_bind(naudas_iznemsana, "<Button-1>", on_rectangle_click)

def ievietot_karti(notikums):
    if notikums.keysym == 'space':
        canvas.delete("all")
        pin_kods = canvas.create_text(vid_x, 140, \
                                      text="Ievadiet PIN kodu", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
        pin_kods_eng = canvas.create_text(vid_x, 210, \
                                      text="Please enter your PIN", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
        pin_kods_ekrans = canvas.create_rectangle(vid_x-250, 270, vid_x+250, 350,
                                outline = "#9F8383", fill = "#9F8383",
                                width = 10)
        pin_kods_keyboard = canvas.create_rectangle(vid_x-400, 450, vid_x+400, 850,
                                outline="#9F8383", fill = "#9F8383",
                                                    width = 10)
        pin_kods_pogas_bg = canvas.create_rectangle(vid_x-370, 480, vid_x-20, 820,
                                outline="#C8AAAA", fill = "#C8AAAA",
                                                    width = 10)
        pin_kods_pogas_bg2 = canvas.create_rectangle(vid_x+20, 480, vid_x+370, 820,
                                outline="#C8AAAA", fill = "#C8AAAA",
                                                    width = 10)
        pin_entry = Entry(canvas, textvariable = pin_var, font=('catamaran',30,'bold'), show = '*')
        canvas.create_window(vid_y+160, 310, window=pin_entry)

        pin_enter_poga = Button(canvas, text ="ENTER", command = apstiprinat_pin, font=('catamaran',25,'bold'))
        canvas.create_window(vid_x+180, 550, window=pin_enter_poga)


canvas.bind_all('<Key>', ievietot_karti)

karte_sakums = canvas.create_text(vid_x, 150, \
              text=f"Lai sāktu darbību, \n ievietojiet karti", fill='#FFFFFF', font=('Catamaran', 50, "bold")) #import font
karte_sakums_eng = canvas.create_text(vid_x, 810, \
              text=f"To proceed, please \n insert your card", fill='#FFFFFF', font=('Catamaran', 50, "bold")) #import font

root.mainloop()
