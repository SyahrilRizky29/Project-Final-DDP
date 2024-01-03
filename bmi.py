from tkinter import *
import tkinter.ttk as ttk
from ttkbootstrap import Style

root = Tk()
style = Style(theme="superhero")

root.geometry("500x500")
root.title("Aplikasi Penghitung Berat Badan")

ttk.Label(root, text="Aplikasi Penghitung Berat Badan", font=("poppins", 15, "bold")).pack(pady=9)
ttk.Label(root, text="Masukan Berat:").pack(pady=10)

berat = Entry()
berat.insert(END, 0)
berat.pack()

ttk.Label(root, text="Masukan Tinggi:").pack(pady=10)

tinggi = Entry()
tinggi.insert(END, 0)
tinggi.pack()

def BMI():
    h = float(tinggi.get())
    w = float(berat.get())

    # convert height into meter
    m = h / 100
    hasil = round(float(w / m ** 2), 1)
    result_label.config(text="BMI: " + str(hasil))

    if hasil <= 18.5:
        status_label.config(text="Kurang Gizi!")
        description_label.config(text="Minimal makan nasi!")

    elif hasil > 18.5 and hasil <= 25:
        status_label.config(text="Kerja Bagus!")
        description_label.config(text="Lanjutkeun Boy!")

    elif hasil > 25 and hasil <= 30:
        status_label.config(text="Puasa bang!")
        description_label.config(text="Biar beras di rumah gk abis!")

    else:
        status_label.config(text="Diet Om!")
        description_label.config(text="Baju dah pada sempit noh")


ttk.Button(root, text="Hitung", command=BMI, style="danger").pack(pady=10)
result_label = ttk.Label(root, text="")
result_label.pack()
status_label = ttk.Label(root, text="")
status_label.pack()
description_label = ttk.Label(root, text="")
description_label.pack()

root.mainloop()