import tkinter as tk
from tkinter import *
from tkinter import messagebox

def calculate():
        endWeight = float(weight.get()) * 10
        endHeight = float(height.get()) * 6.25
        endAge = float(age.get()) * 5
        endSex = float(rb_sex.get())
        endActiv = float(opt_activ.get())

        endPPM = (endWeight + endHeight) - endAge + endSex
        ppm_final = endPPM * endActiv
        messagebox.showinfo("PPM wynosi", +ppm_final)
def bmi_calc():
        bmi = (float(weight.get()) / float(height.get())**2)*10000
        bmi = round(bmi, 2)
        messagebox.showinfo("BMI wynosi:", +bmi)

master = Tk()
master.geometry("500x450")

master.title("Kalkulator dziennego zapotrzebowania kalorycznego i BMI")
tk.Label(master, text="Podaj swoje imię").grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
tk.Label(master, text="Podaj swój wzrost w cm").grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
tk.Label(master, text="Podaj swoją wagę w kg").grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')
tk.Label(master, text="Podaj ile masz lat").grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'nw')

name = tk.Entry(master)
height = tk.Entry(master)
weight = tk.Entry(master)
age = tk.Entry(master)

name.grid(row = 0, column = 1,  padx = 100, pady = 5, sticky = 'w')
height.grid(row = 1, column = 1, padx = 100, pady = 5, sticky = 'w')
weight.grid(row = 2, column = 1,  padx = 100, pady = 5, sticky = 'w')
age.grid(row = 3, column = 1,  padx = 100, pady = 5, sticky = 'w')

rb_sex = tk.IntVar()
tk.Label(master, text="Zaznacz swoją płeć").grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 15, sticky = 'nw')
rb_female = tk.Radiobutton(master, variable = rb_sex, value = (-161), text = "kobieta")
rb_male = tk.Radiobutton(master, variable = rb_sex, value = (+5), text = "mężczyzna")

rb_sex.set(rb_sex)
rb_female.grid(row = 4, column = 1, columnspan = 2, padx = 50, pady = 15, sticky = 'nw')
rb_male.grid(row = 4, column = 1, columnspan = 2, padx = 150, pady = 15, sticky = 'nw')

opt_activ = tk.DoubleVar()
tk.Label(master, text="Zaznacz swoją aktywność fizyczną").grid(row = 10, column = 0, columnspan = 2, padx = 5, pady = 15, sticky = 'nw')
opt1 = tk.Radiobutton(master, variable = opt_activ, value = (1.2), text = "Praca siedząca, brak dodatkowej aktywności fizycznej")
opt2 = tk.Radiobutton(master, variable = opt_activ, value = (1.4), text = "Praca niefizyczna, mało aktywny tryb życia")
opt3 = tk.Radiobutton(master, variable = opt_activ, value = (1.6), text = "Lekka praca fizyczna, regularne ćwiczenia 3-4 razy print(ok. 5h) w tygodniu")
opt4 = tk.Radiobutton(master, variable = opt_activ, value = (1.8), text = "Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu")
opt5 = tk.Radiobutton(master, variable = opt_activ, value = (2.0), text = "Praca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu ")

opt_activ.set(opt1)
opt1.grid(row = 11, column = 0, columnspan = 2, sticky = 'nw', padx = 5, pady = 5)
opt2.grid(row = 12, column = 0, columnspan = 2, sticky = 'nw', padx = 5, pady = 5)
opt3.grid(row = 13, column = 0, columnspan = 2, sticky = 'nw', padx = 5, pady = 5)
opt4.grid(row = 14, column = 0, columnspan = 2, sticky = 'nw', padx = 5, pady = 5)
opt5.grid(row = 15, column = 0, columnspan = 2, sticky = 'nw', padx = 5, pady = 5)

tk.Button(master, text="Oblicz PPM", command=calculate).grid(row = 17, column = 0, columnspan = 2, sticky='nw', padx=20, pady=15)
tk.Button(master, text="Oblicz BMI",command=bmi_calc).grid(row = 17, column = 0, columnspan = 2, sticky='nw', padx=150, pady=15)
tk.Button(master, text="Wyjście", command=master.quit).grid(row = 17, column = 0, columnspan = 2, sticky='nw', padx=300, pady=15)
tk.mainloop()

