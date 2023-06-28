import tkinter as tk, matplotlib.pyplot as plt, json
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

# ANIMACIÓN
def animacion():
    global background_photo, car_photo        
    canvas = tk.Canvas(ventana, width=700, height=150)
    canvas.place(x=386, y=5)

    background_image = Image.open("road3.png")
    background_photo = ImageTk.PhotoImage(background_image)

    background1 = canvas.create_image(0, 0, image=background_photo, anchor="nw")
    background2 = canvas.create_image(700, 0, image=background_photo, anchor="nw")

    car_image = Image.open("car.png")
    car_image = car_image.resize((80, 100), Image.ANTIALIAS)
    car_photo = ImageTk.PhotoImage(car_image)
    car = canvas.create_image(300, 120, image=car_photo)

    def move_background():
        canvas.move(background1, -100, 0)
        canvas.move(background2, -100, 0)
        if canvas.coords(background1)[0] < -700:
            canvas.move(background1, 1400, 0)
        if canvas.coords(background2)[0] < -700:
            canvas.move(background2, 1400, 0)
        canvas.after(60, move_background)

    move_background()
# GRAFICO
def graficos(dato):
    fig1 = plt.figure(figsize=(4.32,3), dpi=100)
    ax1 = fig1.add_subplot(111)
    fig2 = plt.figure(figsize=(4.32,3), dpi=100)
    ax2 = fig2.add_subplot(111)
    if dato == "pos":
        ax1.plot([0, t], [0, posi])
        ax2.plot([0, t], [v,v])
    elif dato == "vel":
        ax1.plot([tI, tF], [xI, xF])
        ax2.plot([tI, tF], [div,div])
    elif dato == "tie":
        ax1.plot([0, tiem], [0, x])
        ax2.plot([0, tiem], [v, v])
    ax1.set_title('Grafico Posición - Tiempo')
    ax1.set(xlabel='T (s)', ylabel='X (m)')
    ax1.grid(color='black', linestyle='--', linewidth=0.5)
    fig1.tight_layout()

    ax2.set_title('Grafico Velocidad - Tiempo')
    ax2.set(xlabel='T (s))', ylabel='V (m/s)')
    ax2.grid(color='black', linestyle='--', linewidth=0.5)
    fig2.tight_layout()

    canvas1 = FigureCanvasTkAgg(fig1, master=ventana)
    canvas2 = FigureCanvasTkAgg(fig2, master=ventana)

    canvas1.draw()
    canvas2.draw()
    canvas1.get_tk_widget().place(x=391, y=176)
    canvas2.get_tk_widget().place(x=838, y=176)

def fondo_btn(dato):
    btn_body = Frame(ventana, bg='#FFEBC9')
    btn_body.place(x=25, y=365, width=326, height=305)

    btn_header = Label(ventana, text='Ingrese los siguientes datos: ', bg='#211717', fg='#fff')
    btn_header.place(x=25, y=365, width=326)
    
    if dato == "posicion":
        enviar_btn = Button(ventana, text='Guardar', bg='#DFDDC7', command=pos)
    elif dato == "velocidad":
        enviar_btn = Button(ventana, text='Guardar', bg='#DFDDC7', command=vel)
    elif dato == "tiempo":
        enviar_btn = Button(ventana, text='Guardar', bg='#DFDDC7', command=tie)
    enviar_btn.place(x=138, y=497, width=100)
def posicion():
    global v_box, t_box, seleccion
    fondo_btn("posicion")
    definicion.configure(text=defi_posicion)
    v = Label(ventana, text= "Ingrese velocidad en m/s", fg="#000", bg="#FFEBC9")
    t = Label(ventana, text= "Ingrese tiempo en s:", fg="#000", bg="#FFEBC9")   
    v.place(x=44, y=391)
    t.place(x=44, y=412)

    v_box = Entry(ventana)
    v_box.place(x=208, y=391)
    t_box = Entry(ventana)
    t_box.place(x=208, y=412)
    ventana.mainloop()

def velocidad():
    global xI_box, xF_box, tI_box, tF_box, seleccion
    fondo_btn("velocidad")
    definicion.configure(text=defi_velocidad)
    xI_lbl = Label(ventana, text= "Ingrese posicion inicial en m:", fg="#000", bg="#FFEBC9")
    xF_lbl = Label(ventana, text= "Ingrese posicion final en m:", fg="#000", bg="#FFEBC9")   
    xI_lbl.place(x=44, y=391)
    xF_lbl.place(x=44, y=412)

    tI_lbl = Label(ventana, text= "Ingrese tiempo inicial en s :", fg="#000", bg="#FFEBC9")
    tF_lbl = Label(ventana, text= "Ingrese tiempo final en s :", fg="#000", bg="#FFEBC9")
    tI_lbl.place(x=44, y=433)
    tF_lbl.place(x=44, y=454)
    xI_box = Entry(ventana)
    xI_box.place(x=208, y=391)
    xF_box = Entry(ventana)
    xF_box.place(x=208, y=412)
    tI_box = Entry(ventana)
    tI_box.place(x=208, y=433)
    tF_box = Entry(ventana)
    tF_box.place(x=208, y=454)
    ventana.mainloop()

def tiempo():
    global x_box, v_box
    fondo_btn("tiempo")
    definicion.configure(text=defi_tiempo)
    x = Label(ventana, text= "Ingrese distancia en m: ", fg="#000", bg="#FFEBC9")
    v = Label(ventana, text= "Ingrese velocidad en m/s:", fg="#000", bg="#FFEBC9")   
    x.place(x=44, y=391)
    v.place(x=44, y=412)

    x_box = Entry(ventana)
    x_box.place(x=208, y=391)
    v_box = Entry(ventana)
    v_box.place(x=208, y=412)
    ventana.mainloop()

def pos():
    global v, t, posi
    v = float(v_box.get())
    t = float(t_box.get())
    posi = v * t
    total = f'La posición final sera {posi} metros.'
    posicion_f = Label(ventana, text=total, bg='#FFEBC9')
    posicion_f.place(x=93, y=547)
    graficos("pos")
    animacion()

def vel():
    global xI, xF, tI, tF, div
    xI = float(xI_box.get())
    xF = float(xF_box.get())
    tI = float(tI_box.get())
    tF = float(tF_box.get())
    div = (xF - xI) / (tF - tI)
    total = f'La velocidad constante sera de {div} m/s'
    vel_final = Label(ventana, text=total, bg='#FFEBC9')
    vel_final.place(x=93, y=547)
    graficos("vel")
    animacion()

def tie():
    global x, v, tiem
    x = float(x_box.get())
    v = float(v_box.get())
    tiem = x / v
    total = f'El tiempo final es de {tiem} s.'
    tie_final = Label(ventana, text=total, bg='#FFEBC9')
    tie_final.place(x=93, y=547)
    graficos("tie")
    animacion()





# VENTANA
ventana = tk.Tk()
ventana.title('Movimiento Rectilíneo Uniforme (MRU)')
ventana.geometry('1280x700')
ventana.resizable(False, False)
ventana.configure(bg='#DFDDC7') 

# TEXTOS
with open('textos/textos.json', 'r', encoding='utf-8') as textos:
    contenido_mru = json.load(textos)
# Definicion general
var_mru = contenido_mru
def_general = var_mru[0]['def_mru']

# Definiciones para variables
defi_velocidad = var_mru[0]['defi_velocidad']
defi_posicion = var_mru[0]['defi_posicion']
defi_tiempo = var_mru[0]['defi_tiempo']

# Definiciones para graficos
defi_grafico_velocidad = var_mru[1]['defi_grafico_velocidad']
defi_grafico_posicion = var_mru[1]['defi_grafico_posicion']
defi_grafico_tiempo = var_mru[1]['defi_grafico_tiempo']

# MAIN BACKGROUND
body = Frame(ventana, bg='#A34A28')
header = Label(ventana, text='Bienvenido a la aplicación <<<-MRU->>>', bg='#211717', fg='#fff')
definicion = Label(ventana, text=def_general, bg='#C38154', fg='#fff', wraplength=290)
pregunta = Label(ventana, text='¿Qué desea calcular?', bg='#211717', fg='#fff')
split = Frame(ventana, bg='#211717')

# BOTONES
btn_bg = Frame(ventana, bg='#C38154')
btn_pos = Button(ventana, text='Posicion recorrida', bg='#DFDDC7', command=posicion)
btn_v = Button(ventana, text='Velocidad constante', bg='#DFDDC7', command=velocidad)
btn_t = Button(ventana, text='Tiempo total', bg='#DFDDC7', command=tiempo)

body.place(x=5, y=5, width=366, height=690)
header.place(x=5, y=5, width=366, height=42)
definicion.place(x = 38, y = 57, width= 300, height= 140)
pregunta.place(x=5, y=207, width=366, height=35)
split.place(x=376, y=0, width=5, height=700)
btn_bg.place(x=15, y=255, width=346, height=430)
btn_pos.place(x=25, y=265, width=326, height=25)
btn_v.place(x=25, y=295, width=326, height=25)
btn_t.place(x=25, y=325, width=326, height=25)
# MAIN GRAFICOS / DATOS
header_animado = Frame(bg='#A34A28')
graph_body1 = Frame(bg='#A34A28')
graph_body2 = Frame(bg='#A34A28')
graph_datos1 = Frame(bg='#C38154')
graph_datos2 = Frame(bg='#C38154')

header_animado.place(x=386, y=5, width=888, height=150)
graph_body1.place(x=386, y=171, width=442, height=524)
graph_body2.place(x=833, y=171, width=442, height=524)
graph_datos1.place(x=391, y=476, width=432, height=150)
graph_datos2.place(x=838, y=476, width=432, height=150)


ventana.mainloop()