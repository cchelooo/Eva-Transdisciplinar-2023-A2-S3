import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
# FUNCIONES PRINCIPALES
def distancia():
    return
def velocidad():
    return
def tiempo():
    return
def info():
    window = tk.Toplevel(ventana)
    window.geometry("750x500")
    window.configure(bg='grey')

    tlLbl = tk.Label(window, text='El movimiento rectilineo uniforme (M.R.U)')
    tlLbl.pack()
    defLbl = tk.Label(window, text='El el mru.....')
    defLbl.pack()
    window.mainloop()
    return

def ventanas():
    # VENTANA
    global ventana
    ventana = tk.Tk()
    ventana.title('Movimiento uniforme rectilineo (MUR)')
    ventana.geometry("1200x600")
    ventana.resizable(False, False)
    ventana.configure(bg='#393053')
    
    # LABELS IZQ
    texto1 = tk.Label(ventana, text="El movimiento rectilino uniforme, es el movimiento de un objeto ,\n que viaja en una tayectoria de linia recta con velocidad constante").place(x=50, y=50)
    infBtn = tk.Button(ventana, text='Mas información...', command=info)
    infBtn.place(x=50, y=100)
    selecTxt = tk.Label(ventana, text='¿Qué desea calcular?').place(x=50,y=300)
    dBtn = tk.Button(ventana, text='Distancia = Velocidad * Tiempo', command='', width=45, height=2)
    dBtn.place(x=50, y=350)
    vBtn = tk.Button(ventana, text='Velocidad = Distancia / Tiempo', command='', width=45, height=2)
    vBtn.place(x=50, y=400)
    tBtn = tk.Button(ventana, text='Tiempo = Distancia / Velocidad', command='', width=45, height=2)
    tBtn.place(x=50, y=450)
    
    # LABELS DER
    txtLbl1 = tk.Label(ventana, text='Selecciona una opción').place(x=550,y=30)
    txtLbl2 = tk.Label(ventana, text='N/A').place(x=550, y=60)
    txtEnt1 = tk.Entry(ventana)
    txtEnt1.place(x=620, y=60)
    txtLbl3 = tk.Label(ventana, text='N/A').place(x=550, y=90)
    txtEnt2 = tk.Entry(ventana)
    txtEnt2.place(x=620, y=90)
    
    # GRAFICO
    fig = plt.figure(figsize=(6,4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot()
    ax.set(xlim=[0,3], ylim=[0,3], xlabel='X', ylabel='Y')
    ax.grid(color='black', linestyle='--', linewidth=0.5)
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().place(x=550, y=155, width=600, height=400)
    ventana.mainloop()
    return
while True:
    ventanas()