from tkinter import *
from tkinter import font
from tkinter import messagebox
import time

platums = 1280
garums = 960
root = Tk()
root.title("Bankomāts")

Catamaran = font.Font(family="Catamaran-Bold", size=80, weight="bold")

pin_var=StringVar()

vid_x = platums / 2
vid_y = garums / 2

canvas = None #deklarēt canvas kā globālu

def sakuma_ekrans(event=None):
    global canvas
    if canvas:
        canvas.destroy()
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    canvas.bind_all('<Key>', ievietot_karti)

    karte_sakums = canvas.create_text(vid_x, 150, text="Lai sāktu darbību, \n ievietojiet karti", fill='#FFFFFF', font=('Catamaran', 50, "bold"))
    karte_sakums_eng = canvas.create_text(vid_x, 810, text="To proceed, please \n insert your card", fill='#FFFFFF', font=('Catamaran', 50, "bold"))

def meklet_pin():
    try:
        with open("pareizais_kods.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "PIN file not found!")
        return None

def apstiprinat_pin():
    global canvas
    uzglabatais_pin = meklet_pin()
    ievaditais_pin = pin_var.get()

    if uzglabatais_pin is None:
        return
    
    if ievaditais_pin == uzglabatais_pin:
        canvas.destroy()
        darijuma_ekrans()
    else:
        canvas.destroy()
        nepareizais_pin_ekrans()

def naudas_iznemsana_click(event):
    canvas.destroy()
    iznemsanas_ekrans()

def naudas_iemaksa_click(event):
    print("Naudas iemaksa!")

def bilance_click(event):
    print("Bilance!")

def cita_operacija_click(event):
    print("Cita operācija!")

def gaidisanas_ekrans_click(event=None):
    canvas.destroy()
    gaidisanas_ekrans()
    root.after(5000, ceka_ekrans)

def nepareizs_pin_ja(event=None):
    canvas.destroy()
    pin_koda_ekrans()

def nepareizs_pin_ne(event=None):
    canvas.destroy()
    sakuma_ekrans()

def gaidisanas_ekrans_ceks_click(event=None):
    canvas.destroy()
    gaidisanas_ekrans()
    root.after(5000, darijums_pabeigts)

def ceks_ne_click(event=None):
    canvas.destroy()
    darijums_pabeigts()

def darijuma_ekrans_click(event=None):
    canvas.destroy()
    darijuma_ekrans()

def darijuma_ekrans():
    global canvas 
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    noradit_darijumu = canvas.create_text(vid_x, 140, \
                                      text="Lūdzu, norādiet darījumu!", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    noradit_darijumu_eng = canvas.create_text(vid_x, 210, \
                                      text="Please select an option!", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    naudas_iznemsana = canvas.create_rectangle(0, vid_y-35, 500, vid_y+35,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    naudas_iznemsana_teksts = canvas.create_text(480, vid_y, \
                                                 text="Naudas izņemšana", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="e")
    canvas.tag_bind(naudas_iznemsana, "<Button-1>", naudas_iznemsana_click)

    naudas_iemaksa = canvas.create_rectangle(0, vid_y+100, 500, vid_y+170,
                                             outline="#786689", fill = "#786689",
                                             width = 10)
    naudas_iemaksa_teksts = canvas.create_text(480, vid_y+135, \
                                               text="Naudas iemaksa", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                               anchor="e")
    canvas.tag_bind(naudas_iemaksa, "<Button-1>", naudas_iemaksa_click)

    bilance = canvas.create_rectangle(780, vid_y-35, 1280, vid_y+35,
                                      outline="#786689", fill = "#786689",
                                      width = 10)
    bilance_teksts = canvas.create_text(800, vid_y, \
                                        text="Bilance", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                        anchor="w")
    canvas.tag_bind(bilance, "<Button-1>", bilance_click)

    cita_operacija = canvas.create_rectangle(780, vid_y+100, 1280, vid_y+170,
                                             outline="#786689", fill = "#786689",
                                             width = 10)
    cita_operacija_teksts = canvas.create_text(800, vid_y+135, \
                                               text="Cita operācija", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                               anchor="w")
    canvas.tag_bind(cita_operacija, "<Button-1>", cita_operacija_click)

def iznemsanas_ekrans():
    global canvas 
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    noradit_summu = canvas.create_text(vid_x, 140, \
                                      text="Lūdzu, norādiet summu!", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    noradit_summu_eng = canvas.create_text(vid_x, 210, \
                                      text="Select a withdrawal amount!", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    
    pieci_eiro = canvas.create_rectangle(0, vid_y-140, 500, vid_y-70,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    pieci_eiro_teksts = canvas.create_text(480, vid_y-105, \
                                                 text="5 EUR", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="e")
    canvas.tag_bind(pieci_eiro, "<Button-1>", gaidisanas_ekrans_click)

    desmit_eiro = canvas.create_rectangle(0, vid_y-5, 500, vid_y+65,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    desmit_eiro_teksts = canvas.create_text(480, vid_y+30, \
                                                 text="10 EUR", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="e")
    canvas.tag_bind(desmit_eiro, "<Button-1>", gaidisanas_ekrans_click)

    divdesmit_eiro = canvas.create_rectangle(0, vid_y+130, 500, vid_y+200,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    divdesmit_eiro_teksts = canvas.create_text(480, vid_y+165, \
                                                 text="20 EUR", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="e")
    canvas.tag_bind(divdesmit_eiro, "<Button-1>", gaidisanas_ekrans_click)

    piecdesmit_eiro = canvas.create_rectangle(0, vid_y+265, 500, vid_y+335,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    piecdesmit_eiro_teksts = canvas.create_text(480, vid_y+300, \
                                                 text="50 EUR", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="e")
    canvas.tag_bind(piecdesmit_eiro, "<Button-1>", gaidisanas_ekrans_click)

    simts_eiro = canvas.create_rectangle(780, vid_y-140, 1280, vid_y-70,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    simts_eiro_teksts = canvas.create_text(800, vid_y-105, \
                                                 text="100 EUR", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="w")
    canvas.tag_bind(simts_eiro, "<Button-1>", gaidisanas_ekrans_click)

    cita_summa = canvas.create_rectangle(780, vid_y-5, 1280, vid_y+65,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    cita_summa_teksts = canvas.create_text(800, vid_y+30, \
                                                 text="Cita summa", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="w")
    canvas.tag_bind(cita_summa, "<Button-1>", gaidisanas_ekrans_click)

    bilance2 = canvas.create_rectangle(780, vid_y+130, 1280, vid_y+200,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    bilance2_teksts = canvas.create_text(800, vid_y+165, \
                                                 text="Bilance", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="w")
    canvas.tag_bind(bilance2, "<Button-1>", gaidisanas_ekrans_click)

    cita_operacija2 = canvas.create_rectangle(780, vid_y+265, 1280, vid_y+335,
                                               outline="#786689", fill = "#786689",
                                               width = 10)
    cita_operacija2_teksts = canvas.create_text(800, vid_y+300, \
                                                 text="Cita operācija", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                 anchor="w")
    canvas.tag_bind(cita_operacija2, "<Button-1>", gaidisanas_ekrans_click)
    
def gaidisanas_ekrans():
    global canvas 
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    ludzu_uzgaidiet = canvas.create_text(vid_x, vid_y-50, \
                                      text="Lūdzu, uzgaidiet", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    ludzu_uzgaidiet_eng = canvas.create_text(vid_x, vid_y+15, \
                                      text="Please wait", fill="#FFFFFF", font=('Catamaran', 30, "bold"))

def ceka_ekrans():
    global canvas
    if canvas:
        canvas.destroy()
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    ceka_izvele = canvas.create_text(vid_x, 140, \
                                      text="Vai vēlaties čeku?", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    ceka_izvele_eng = canvas.create_text(vid_x, 210, \
                                      text="Print out check?", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    izvele_ja2 = canvas.create_rectangle(780, vid_y-35, 1280, vid_y+35,
                                                         outline="#786689", fill = "#786689",
                                                         width = 10)
    izvele_ja2_teksts = canvas.create_text(800, vid_y, \
                                                         text="Jā", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                         anchor="w")
    canvas.tag_bind(izvele_ja2, "<Button-1>", gaidisanas_ekrans_ceks_click)

    izvele_ne2 = canvas.create_rectangle(780, vid_y+100, 1280, vid_y+170,
                                                         outline="#786689", fill = "#786689",
                                                         width = 10)
    izvele_ne2_teksts = canvas.create_text(800, vid_y+135, \
                                                         text="Nē", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                         anchor="w")
    canvas.tag_bind(izvele_ne2, "<Button-1>", ceks_ne_click)

def darijums_pabeigts():
    global canvas
    if canvas:
        canvas.destroy()
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    darijums_pabeigts = canvas.create_text(vid_x, 140, \
                                      text=f"Darījums pabeigts!", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    darijums_pabeigts2 = canvas.create_text(vid_x, 220, \
                                      text=f"Vai vēlaties citu darījumu?", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    darijums_pabeigts_eng = canvas.create_text(vid_x, 290, \
                                      text="Transaction finished!", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    darijums_pabeigts2_eng = canvas.create_text(vid_x, 330, \
                                      text="Choose another transaction?", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    izvele_ja3 = canvas.create_rectangle(780, vid_y-35, 1280, vid_y+35,
                                                         outline="#786689", fill = "#786689",
                                                         width = 10)
    izvele_ja3_teksts = canvas.create_text(800, vid_y, \
                                                         text="Jā", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                         anchor="w")
    canvas.tag_bind(izvele_ja3, "<Button-1>", darijuma_ekrans_click)

    izvele_ne3 = canvas.create_rectangle(780, vid_y+100, 1280, vid_y+170,
                                                         outline="#786689", fill = "#786689",
                                                         width = 10)
    izvele_ne3_teksts = canvas.create_text(800, vid_y+135, \
                                                         text="Nē", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                         anchor="w")
    canvas.tag_bind(izvele_ne3, "<Button-1>", sakuma_ekrans)

def nepareizais_pin_ekrans():
    global canvas
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    noradit_darijumu = canvas.create_text(vid_x, 140, \
                                      text="Nepareizais PIN. Mēģināt vēlreiz?", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    noradit_darijumu_eng = canvas.create_text(vid_x, 210, \
                                      text="Incorrect PIN. Try again?", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    izvele_ja = canvas.create_rectangle(780, vid_y-35, 1280, vid_y+35,
                                                         outline="#786689", fill = "#786689",
                                                         width = 10)
    izvele_ja_teksts = canvas.create_text(800, vid_y, \
                                                         text="Jā", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                         anchor="w")
    canvas.tag_bind(izvele_ja, "<Button-1>", nepareizs_pin_ja)

    izvele_ne = canvas.create_rectangle(780, vid_y+100, 1280, vid_y+170,
                                                         outline="#786689", fill = "#786689",
                                                         width = 10)
    izvele_ne_teksts = canvas.create_text(800, vid_y+135, \
                                                         text="Nē", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                         anchor="w")
    canvas.tag_bind(izvele_ne, "<Button-1>", nepareizs_pin_ne)

def pin_koda_ekrans():
    global canvas
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()
        
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

def ievietot_karti(notikums):
    if notikums.keysym == 'space':
        if canvas:
            canvas.destroy()
        pin_koda_ekrans()

sakuma_ekrans() #sākt ar kāršu ievietošanas ekrānu

root.mainloop()