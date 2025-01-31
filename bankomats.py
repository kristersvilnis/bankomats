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

    karte_sakums = canvas.create_text(vid_x, 100, text="Lai sāktu darbību,", fill='#FFFFFF', font=('Catamaran', 50, "bold"), anchor="center")
    karte_sakums2 = canvas.create_text(vid_x, 180, text="ievietojiet karti", fill='#FFFFFF', font=('Catamaran', 50, "bold"), anchor="center")
    karte_sakums_eng = canvas.create_text(vid_x, 810, text="To proceed, please", fill='#FFFFFF', font=('Catamaran', 50, "bold"), anchor="center")
    karte_sakums2_eng = canvas.create_text(vid_x, 890, text="insert your card", fill='#FFFFFF', font=('Catamaran', 50, "bold"), anchor="center")

def meklet_pin():
    try:
        with open("pareizais_kods.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "PIN file not found!")
        return None

def apstiprinat_pin(event=None):
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

def enter_poga_click(event=None):
    canvas.destroy()
    iznemsanas_ekrans()

def dzest_pin(event=None):
    pin_var.set("")

def naudas_iznemsana_click(event):
    canvas.destroy()
    iznemsanas_ekrans()

def naudas_iemaksa_click(event):
    print("Naudas iemaksa!")

def bilance_click(event):
    canvas.destroy()
    gaidisanas_ekrans()
    root.after(1500, bilances_ekrans)

def bilance_summa():
    bilance_fails = open('bilance.txt', 'r')
    bilance_eiro = bilance_fails.read()
    bilance_summa_teksts = canvas.create_text(vid_x, vid_y-150, \
                                      text=f"{bilance_eiro} EUR", fill="#FFFFFF", font=('Catamaran', 60, "bold"))

def cita_operacija_click(event):
    canvas.destroy()
    darijuma_ekrans()

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

def ievietot_karti(notikums):
    if notikums.keysym == 'space':
        if canvas:
            canvas.destroy()
        pin_koda_ekrans()

def pin_koda_ekrans():
    global canvas, pin_entry
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    pin_var.set("")

    pin_kods = canvas.create_text(vid_x, 140, \
                                      text="Ievadiet PIN kodu", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    pin_kods_eng = canvas.create_text(vid_x, 210, \
                                      text="Please enter your PIN", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    pin_kods_ekrans = canvas.create_rectangle(vid_x-250, 270, vid_x+250, 350,
                                              outline = "#9F8383", fill = "#9F8383",
                                              width = 10)
    pin_kods_keyboard = canvas.create_rectangle(vid_x-250, 450, vid_x+250, 830,
                                                outline="#9F8383", fill = "#9F8383",
                                                width = 10)
    pin_kods_pogas_bg2 = canvas.create_rectangle(vid_x-220, 480, vid_x+220, 800,
                                                 outline="#C8AAAA", fill = "#C8AAAA",
                                                 width = 10)
    pin_entry = Entry(canvas, textvariable = pin_var, font=('catamaran',30,'bold'), show = '*')
    canvas.create_window(vid_y+160, 310, window=pin_entry)
    # ENTER poga
    pin_enter_poga = canvas.create_rectangle(vid_x-210, 490, vid_x+210, 550,
                                                         outline="#EEEEEE", fill = "#EEEEEE",
                                                         width = 10)
    pin_enter_teksts = canvas.create_text(vid_x-190, 520, \
                                                         text="Enter", fill="#000000", font=('Catamaran', 25, "bold"),
                                                         anchor="w")
    pin_enter_poga_ikona = canvas.create_line(vid_x-190, 540, vid_x-100, 540, fill="#2EC301", width=5)
    pin_enter_poga_aplis = canvas.create_oval(vid_x+150, 500, vid_x+190, 540, outline="black", width=5)
    canvas.tag_bind(pin_enter_poga, "<Button-1>", apstiprinat_pin)
    canvas.tag_bind(pin_enter_teksts, "<Button-1>", apstiprinat_pin)
    canvas.tag_bind(pin_enter_poga_ikona, "<Button-1>", apstiprinat_pin)
    canvas.tag_bind(pin_enter_poga_aplis, "<Button-1>", apstiprinat_pin)

    # CLEAR poga
    pin_clear_poga = canvas.create_rectangle(vid_x-210, 570, vid_x+210, 630,
                                                         outline="#EEEEEE", fill = "#EEEEEE",
                                                         width = 10)
    pin_clear_teksts = canvas.create_text(vid_x-190, 600, \
                                                         text="Clear", fill="#000000", font=('Catamaran', 25, "bold"),
                                                         anchor="w")
    pin_clear_poga_ikona = canvas.create_line(vid_x-190, 620, vid_x-100, 620, fill="#E7DF00", width=5)
    pin_clear_poga_trissturis = canvas.create_polygon(vid_x+150, 600, vid_x+180, 580, vid_x+150, 600, vid_x+180, 620, outline="black", width=5)
    canvas.tag_bind(pin_clear_poga, "<Button-1>", dzest_pin)
    canvas.tag_bind(pin_clear_teksts, "<Button-1>", dzest_pin)
    canvas.tag_bind(pin_clear_poga_ikona, "<Button-1>", dzest_pin)
    canvas.tag_bind(pin_clear_poga_trissturis, "<Button-1>", dzest_pin)
    # CANCEL poga
    pin_cancel_poga = canvas.create_rectangle(vid_x-210, 650, vid_x+210, 710,
                                                         outline="#EEEEEE", fill = "#EEEEEE",
                                                         width = 10)
    pin_cancel_teksts = canvas.create_text(vid_x-190, 680, \
                                                         text="Cancel", fill="#000000", font=('Catamaran', 25, "bold"),
                                                         anchor="w")
    pin_clear_poga_ikona = canvas.create_line(vid_x-190, 700, vid_x-100, 700, fill="#E70000", width=5)
    pin_clear_poga_linija1 = canvas.create_line(vid_x+148, 660, vid_x+192, 700, fill="black", width=5)
    pin_clear_poga_linija2 = canvas.create_line(vid_x+192, 660, vid_x+148, 700, fill="black", width=5)
    canvas.tag_bind(pin_cancel_poga, "<Button-1>", sakuma_ekrans)
    canvas.tag_bind(pin_cancel_teksts, "<Button-1>", sakuma_ekrans)
    canvas.tag_bind(pin_clear_poga_ikona, "<Button-1>", sakuma_ekrans)
    canvas.tag_bind(pin_clear_poga_linija1, "<Button-1>", sakuma_ekrans)
    canvas.tag_bind(pin_clear_poga_linija2, "<Button-1>", sakuma_ekrans)
    # tukšs lauks
    tukss_lauks = canvas.create_rectangle(vid_x-210, 730, vid_x+210, 790,
                                                         outline="#EEEEEE", fill = "#EEEEEE",
                                                         width = 10)
    

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
    canvas.tag_bind(izvele_ja, "<Button-1>", izvele_ja_teksts)

    izvele_ne = canvas.create_rectangle(780, vid_y+100, 1280, vid_y+170,
                                                         outline="#786689", fill = "#786689",
                                                         width = 10)
    izvele_ne_teksts = canvas.create_text(800, vid_y+135, \
                                                         text="Nē", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                                         anchor="w")
    canvas.tag_bind(izvele_ne, "<Button-1>", nepareizs_pin_ne)
    canvas.tag_bind(izvele_ja, "<Button-1>", izvele_ne_teksts)

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
    canvas.tag_bind(naudas_iznemsana_teksts, "<Button-1>", naudas_iznemsana_click)

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
    canvas.tag_bind(bilance_teksts, "<Button-1>", bilance_click)

    cita_operacija = canvas.create_rectangle(780, vid_y+100, 1280, vid_y+170,
                                             outline="#786689", fill = "#786689",
                                             width = 10)
    cita_operacija_teksts = canvas.create_text(800, vid_y+135, \
                                               text="Iziet", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                               anchor="w")
    canvas.tag_bind(cita_operacija, "<Button-1>", sakuma_ekrans)
    canvas.tag_bind(cita_operacija_teksts, "<Button-1>", sakuma_ekrans)

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

def bilances_ekrans():
    global canvas
    if canvas:
        canvas.destroy()
    canvas = Canvas(root, width=platums, height=garums, bg="#574964")
    canvas.pack()

    darijums_pabeigts = canvas.create_text(vid_x, 140, \
                                      text=f"Jūsu konta atlikums:", fill="#FFFFFF", font=('Catamaran', 50, "bold"))
    darijums_pabeigts_eng = canvas.create_text(vid_x, 210, \
                                      text="Your account balance:", fill="#FFFFFF", font=('Catamaran', 30, "bold"))
    bilance_summa()
    darijums_cita_operacija = canvas.create_rectangle(780, vid_y+65, 1280, vid_y+135,
                                             outline="#786689", fill = "#786689",
                                             width = 10)
    darijums_cita_operacija_teksts = canvas.create_text(800, vid_y+100, \
                                               text="Cita operācija", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                               anchor="w")
    canvas.tag_bind(darijums_cita_operacija, "<Button-1>", cita_operacija_click)
    canvas.tag_bind(darijums_cita_operacija_teksts, "<Button-1>", cita_operacija_click)

    iziet_operacija = canvas.create_rectangle(780, vid_y+200, 1280, vid_y+270,
                                             outline="#786689", fill = "#786689",
                                             width = 10)
    iziet_operacija_teksts = canvas.create_text(800, vid_y+235, \
                                               text="Iziet", fill="#FFFFFF", font=('Catamaran', 30, "bold"),
                                               anchor="w")
    canvas.tag_bind(iziet_operacija, "<Button-1>", sakuma_ekrans)
    canvas.tag_bind(iziet_operacija_teksts, "<Button-1>", sakuma_ekrans)

sakuma_ekrans() #sākt ar kāršu ievietošanas ekrānu

root.mainloop()