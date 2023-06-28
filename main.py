import tkinter as tk, matplotlib.pyplot as plt, json
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

# ANIMACION VELOCIDAD
def animacion(dato):
    global background_photo, car_photo        
    canvas = tk.Canvas(ventana, width=700, height=146)  # Canvas para poder "dibujar" en ella
    canvas.place(x=386, y=5)

    background_image = Image.open("img/road3.png")  # Importar imagen del fondo
    background_photo = ImageTk.PhotoImage(background_image)   # Guardar imagen en variable
    background1 = canvas.create_image(0, 0, image=background_photo, anchor="nw")    # Crear imagen en pos 0, 0
    background2 = canvas.create_image(700, 0, image=background_photo, anchor="nw")  # Crear imagen 2 en pos 700, 0

    car_image = Image.open("img/car.png")   # Importar imagen del auto
    car_image = car_image.resize((80, 100)) # Cambiar tamaño de la imagen
    car_photo = ImageTk.PhotoImage(car_image) # Guardar imagen en variable
    car = canvas.create_image(300, 120, image=car_photo)    # Crear imagen del auto en pos 300, 120

    #FUNCION PARA MOVER EL FONDO
    def move_background():
        if dato == 'pos':                           # Validar selección de boton y sus datos
            canvas.move(background1, -v, 0) # Mover fondo solo en x, a la velocidad elegida.
            canvas.move(background2, -v, 0) # Mover fondo 2 solo en x, a la velocidad elegida.
        elif dato == 'vel':                         # Validar selección de boton y sus datos
            canvas.move(background1, -div, 0) # Mover fondo solo en x, a la velocidad elegida.
            canvas.move(background2, -div, 0) # Mover fondo 2 solo en x, a la velocidad elegida.
        elif dato == 'tie':                         # Validar selección de boton y sus datos
            canvas.move(background1, -v, 0) # Mover fondo solo en x, a la velocidad elegida.
            canvas.move(background2, -v, 0) # Mover fondo 2 solo en x, a la velocidad elegida.
        else:                                       # Estatico
            canvas.move(background1, 0, 0) 
            canvas.move(background2, 0, 0)
            
        # VALIDAR LAS COORDENADAS DE LOS FONDOS PARA REPETIR EN BUCLE
        if canvas.coords(background1)[0] < -700:
            canvas.move(background1, 1400, 0)
        if canvas.coords(background2)[0] < -700:
            canvas.move(background2, 1400, 0)
        canvas.after(60, move_background)

    move_background() # Llamar a la funcion

# TEXTOS DE LA ANIMACION DE VELOCIDAD
def velo_animacion(dato):
    # TEXTOS DE CALCULOS                                                                                                                                
    if dato == 'pos':
        vel_anima.configure(text=f'  v = Δx / Δt\n  v = ({posi} - {0}) / ({t} - {0})\n  v = {v}m/s', font=("Bonodi", 10, "bold italic"), bg='#DFDDC7', justify=LEFT, anchor='w') # Cambiar texto a nuevos datos
    elif dato == 'vel':
        vel_anima.configure(text=f'  v = Δx / Δt\n  v = ({xF} - {xI}) / ({tF} - {tI})\n  v = {div}m/s', font=("Bonodi", 10, "bold italic"), bg='#DFDDC7', justify=LEFT, anchor='w') # Cambiar texto a nuevos datos
    elif dato == 'tie':
        vel_anima.configure(text=f'  v = Δx / Δt\n  v = ({x} - {0}) / ({tiem} - {0})\n  v = {v}m/s', font=("Bonodi", 10, "bold italic"), bg='#DFDDC7', justify=LEFT, anchor='w') # Cambiar texto a nuevos datos
# FONDO DE LOS BOTONES
def fondo_btn(dato):
    global total
    btn_body = Frame(ventana, bg='#FFEBC9') # Fondo de los botones
    btn_body.place(x=25, y=365, width=326, height=305)

    btn_header = Label(ventana, text='Ingrese los siguientes datos: ', bg='#211717', fg='#fff') # Header de los botones
    btn_header.place(x=25, y=365, width=326)

    total = Label(ventana, text='', bg='#FFEBC9')   # Texto de los datos.
    total.place(x=93, y=547)
    animacion('')   # Cargar funcion animacion para que este estatica
    vel_anima.configure(text='INGRESA DATOS', font='TkDefaultFont', justify=CENTER, anchor='center')
    if dato == "posicion":
        enviar_btn = Button(ventana, text='Guardar', bg='#DFDDC7', command=calculo_pos) # Boton enviar POSICION
    elif dato == "velocidad":
        enviar_btn = Button(ventana, text='Guardar', bg='#DFDDC7', command=calculo_vel) # Boton enviar VELOCIDAD
    elif dato == "tiempo":
        enviar_btn = Button(ventana, text='Guardar', bg='#DFDDC7', command=calculo_tie) # Boton enviar TIEMPO
    enviar_btn.place(x=138, y=497, width=100)

# INGRESAR DATOS POSICION
def entry_posicion():
    global v_box, t_box
    fondo_btn("posicion") # Iniciar
    definicion.configure(text=var_mru[0]['defi_posicion'])
    v = Label(ventana, text= "Ingrese velocidad en m/s", fg="#000", bg="#FFEBC9")
    t = Label(ventana, text= "Ingrese tiempo en s:", fg="#000", bg="#FFEBC9")   
    v.place(x=44, y=391)
    t.place(x=44, y=412)

    # validacion de texto
    v_box = Entry(ventana, validate='key', validatecommand=(validacion, '%P'))
    v_box.place(x=208, y=391)
    t_box = Entry(ventana, validate='key', validatecommand=(validacion, '%P'))
    t_box.place(x=208, y=412)
    ventana.mainloop()

# INGRESAR DATOS POSICION
def entry_velocidad():
    global xI_box, xF_box, tI_box, tF_box
    fondo_btn("velocidad")
    definicion.configure(text=var_mru[0]['defi_velocidad'])
    xI_lbl = Label(ventana, text= "Ingrese posicion inicial en m:", fg="#000", bg="#FFEBC9")
    xF_lbl = Label(ventana, text= "Ingrese posicion final en m:", fg="#000", bg="#FFEBC9")   
    xI_lbl.place(x=44, y=391)
    xF_lbl.place(x=44, y=412)

    tI_lbl = Label(ventana, text= "Ingrese tiempo inicial en s :", fg="#000", bg="#FFEBC9")
    tF_lbl = Label(ventana, text= "Ingrese tiempo final en s :", fg="#000", bg="#FFEBC9")
    tI_lbl.place(x=44, y=433)
    tF_lbl.place(x=44, y=454)

    # validacion de texto
    xI_box = Entry(ventana, validate='key', validatecommand=(validacion, '%P'))
    xI_box.place(x=208, y=391)
    xF_box = Entry(ventana, validate='key', validatecommand=(validacion, '%P'))
    xF_box.place(x=208, y=412)
    tI_box = Entry(ventana, validate='key', validatecommand=(validacion, '%P'))
    tI_box.place(x=208, y=433)
    tF_box = Entry(ventana, validate='key', validatecommand=(validacion, '%P'))
    tF_box.place(x=208, y=454)
    ventana.mainloop()

# INGRESAR DATOS TIEMPO
def entry_tiempo():
    global x_box, v_box
    fondo_btn("tiempo")
    definicion.configure(text=var_mru[0]['defi_tiempo'])
    x = Label(ventana, text= "Ingrese distancia en m: ", fg="#000", bg="#FFEBC9")
    v = Label(ventana, text= "Ingrese velocidad en m/s:", fg="#000", bg="#FFEBC9")   
    x.place(x=44, y=391)
    v.place(x=44, y=412)

    x_box = Entry(ventana, validate='key', validatecommand=(validacion, '%P'))
    x_box.place(x=208, y=391)
    v_box = Entry(ventana, validate='key', validatecommand=(validacion, '%P'))
    v_box.place(x=208, y=412)
    ventana.mainloop()

# CALCULO DE POSICION
def calculo_pos():
    global v, t, posi
    mas_info("pos")
    v = float(v_box.get())
    t = float(t_box.get())
    posi = v * t
    posi = round(posi, 2)
    posic = f'La posición final sera {posi} metros.'
    total.configure(text=posic)
    graficos("pos")
    animacion("pos")
    velo_animacion("pos")

# CALCULO DE VELOCIDAD
def calculo_vel():
    global xI, xF, tI, tF, div
    mas_info("vel")
    xI = float(xI_box.get())
    xF = float(xF_box.get())
    tI = float(tI_box.get())
    tF = float(tF_box.get())
    div = (xF - xI) / (tF - tI)
    div = round(div, 2)
    velo = f'La velocidad constante sera de {div} m/s'
    total.configure(text=velo)
    graficos("vel")
    animacion("vel")
    velo_animacion("vel")

# CALCULO DE TIEMPO
def calculo_tie():
    global x, v, tiem
    mas_info("tie")
    x = float(x_box.get())
    v = float(v_box.get())
    tiem = x / v
    tiem = round(tiem, 2)
    tiemp = f'El tiempo final es de {tiem} s.'
    total.configure(text=tiemp)
    graficos("tie")
    animacion("tie")
    velo_animacion("tie")

# BOTON MAS INFO
def mas_info(dato):
    # BOTONES GRAFICOS
    boton = dato
    btn_info1 = Button(ventana, text='Mostrar mas información', bg='#DFDDC7', command=lambda:info("posicion", boton))
    btn_info1.place(x=396, y=596, width=422, height=25)
    btn_info2 = Button(ventana, text='Mostrar mas información', bg='#DFDDC7', command=lambda:info("velocidad", boton))
    btn_info2.place(x=843, y=596, width=422, height=25)

# MAS INFORMACION
def info(dato, boton):
    ventana = tk.Toplevel()
    ventana.title('Información sobre posición')
    ventana.geometry("469x580")
    ventana.configure(bg='#A34A28')
    header = Label(ventana, text='¿Cómo se calculó?', bg='#211717', fg='#fff', font=("Bonodi", 12, "bold italic"))
    header.place(x=0, y=0, width=469, height=50)
    msg = Label(ventana, text=var_mru[2]['importante'], bg='#E0C097', font=("Bonodi", 8, "bold italic"), wraplength=460)
    msg.place(x=3, y=55)
    header_body = Label(ventana, text='¿Qué usaremos?', bg='#211717', fg='#fff', font=("Bonodi", 10, "bold italic"))
    header_body.place(x=3, y=92)
    datos_header = Label(ventana, text='Datos: ', bg='#211717', fg='#fff', font=("Bonodi", 10, "bold italic"))
    datos_header.place(x=3, y=178)
    if dato == "posicion":
        body = Label(ventana, text=var_mru[2]['datos_posicion'], bg='#C38154', fg='#000', font=("Bonodi", 10, "bold italic"))
        body.place(x=3, y=114, width=463)
        calculo = Label(ventana, text='Cálculo: ', bg='#211717', fg='#fff', font=("Bonodi", 10, "bold italic"))
        calculo.place(x=3, y=321)
        bottom = Frame(ventana, bg='#211717')
        bottom.place(x=0, y=515, width=469, height=65)
        if boton == "pos":
            datos = Label(ventana, text=f'\n Velocidad constante: {v}m/s\n\n Tiempo total: {t}s\n\n Posicion final: ???m\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            datos.place(x=3, y=200, width=463)

            calculo_body = Label(ventana, text=f'\nPara calcular la posición usaremos los datos anteriormente dados, elegidos por usted.\nLo que haremos sera multiplicar la velocidad constante por el tiempo total.\n\n    {v} * {t} = {posi}\n\nCon esto listo podemos conocer que la incognita de la posición final es {posi}m.\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            calculo_body.place(x=3, y=343, width=463)
        elif boton == "vel":
            datos = Label(ventana, text=f'\n Velocidad constante: {div}m/s\n\n Tiempo total: {tF}s\n\n Posicion final: ???m\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            datos.place(x=3, y=200, width=463)

            calculo_body = Label(ventana, text=f'\nPara calcular la posición usaremos los datos anteriormente dados, elegidos por usted.\nLo que haremos sera multiplicar la velocidad constante por el tiempo total.\n\n    {div} * {tF} = {xF}\n\nCon esto listo podemos conocer que la incognita de la posición final es {xF}m.\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            calculo_body.place(x=3, y=343, width=463)
        elif boton == "tie":
            datos = Label(ventana, text=f'\n Velocidad constante: {v}m/s\n\n Tiempo total: {tiem}s\n\n Posicion final: ???m\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            datos.place(x=3, y=200, width=463)

            calculo_body = Label(ventana, text=f'\nPara calcular la posición usaremos los datos anteriormente dados, elegidos por usted.\nLo que haremos sera multiplicar la velocidad constante por el tiempo total.\n\n    {v} * {tiem} = {x}\n\nCon esto listo podemos conocer que la incognita de la posición final es {x}m.\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            calculo_body.place(x=3, y=343, width=463)
        # CARGAR IMAGENES EN TKINTER
        img = PhotoImage(file="img\F03.png") 
        img_x = Label(ventana, image=img)
        img_x.place(x=239, y=239)
    elif dato == "velocidad":
        body = Label(ventana, text=var_mru[2]['datos_velocidad'], bg='#C38154', fg='#000', font=("Bonodi", 10, "bold italic"))
        body.place(x=3, y=114, width=463)
        calculo = Label(ventana, text='Cálculo: ', bg='#211717', fg='#fff', font=("Bonodi", 10, "bold italic"))
        calculo.place(x=3, y=381)
        if boton == "pos":
            datos = Label(ventana, text=f'\n Posición inicial: 0m\n\n Posición final: {posi}m\n\n Tiempo inicial: 0s\n\n Tiempo final: {t}s\n\n Velocidad: ???m/s\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            datos.place(x=3, y=200, width=463)

            calculo_body = Label(ventana, text=f'\nPara calcular la velocidad constante usaremos los datos anteriormente dados, \nelegidos por usted.\nLo que haremos sera dividir la posición final con el tiempo total.\n\n   {posi} / {t} = {v}\n\nCon esto realizado podremos conocer que la \nincognita de la velocidad constante es de {v}m/s\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            calculo_body.place(x=3, y=403, width=463)
        elif boton == "vel":
            datos = Label(ventana, text=f'\n Posición inicial: {xI}m\n\n Posición final: {xF}m\n\n Tiempo inicial: {tI}s\n\n Tiempo final: {tF}s\n\n Velocidad: ???m/s\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            datos.place(x=3, y=200, width=463)

            calculo_body = Label(ventana, text=f'\nPara calcular la velocidad constante usaremos los datos anteriormente dados, \nelegidos por usted.\nLo que haremos sera dividir la posición final con el tiempo total.\n\n   {xF} / {tF} = {div}\n\nCon esto realizado podremos conocer que la \nincognita de la velocidad constante es de {v}m/s\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            calculo_body.place(x=3, y=403, width=463)
        elif boton == "tie":
            datos = Label(ventana, text=f'\n Posición inicial: 0m\n\n Posición final: {x}m\n\n Tiempo inicial: 0s\n\n Tiempo final: {tiem}s\n\n Velocidad: ???m/s\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            datos.place(x=3, y=200, width=463)

            calculo_body = Label(ventana, text=f'\nPara calcular la velocidad constante usaremos los datos anteriormente dados, \nelegidos por usted.\nLo que haremos sera dividir la posición final con el tiempo total.\n\n   {x} / {tiem} = {v}\n\nCon esto realizado podremos conocer que la \nincognita de la velocidad constante es de {v}m/s\n', bg='#DFDDC7', justify=LEFT, anchor='w')
            calculo_body.place(x=3, y=403, width=463)

        # CARGAR IMAGENES EN TKINTER
        img = PhotoImage(file="img\F04.png")
        img_v = Label(ventana, image=img)
        img_v.place(x=239, y=260)
    ventana.mainloop()

def ingreso_texto(text):
    if text.count(',') <= 1 and all(char.isdigit() or char == ',' for char in text) or text == "":
        return True
    else:
        return False
# VENTANA
ventana = tk.Tk()
ventana.title('Movimiento Rectilíneo Uniforme (MRU)')
ventana.geometry('1280x700')
ventana.resizable(False, False)
ventana.configure(bg='#DFDDC7') 

validacion = ventana.register(ingreso_texto)

# TEXTOS
with open('json/textos.json', 'r', encoding='utf-8') as textos:
    contenido_mru = json.load(textos)
# Definicion general
var_mru = contenido_mru

# MAIN BACKGROUND
body = Frame(ventana, bg='#A34A28')
header = Label(ventana, text='Bienvenido a la aplicación <<<-MRU->>>', bg='#211717', fg='#fff')
definicion = Label(ventana, text=var_mru[0]['def_mru'], bg='#C38154', fg='#fff', wraplength=290)
pregunta = Label(ventana, text='¿Qué desea calcular?', bg='#211717', fg='#fff')
split = Frame(ventana, bg='#211717')

# UBICACION MAIN BACKGROUND
body.place(x=5, y=5, width=366, height=690)
header.place(x=5, y=5, width=366, height=42)
definicion.place(x = 38, y = 57, width= 300, height= 140)
pregunta.place(x=5, y=207, width=366, height=35)
split.place(x=376, y=0, width=5, height=700)

# BOTONES MAIN
btn_bg = Frame(ventana, bg='#C38154')
btn_pos = Button(ventana, text='Posicion recorrida', bg='#DFDDC7', command=entry_posicion)
btn_v = Button(ventana, text='Velocidad constante', bg='#DFDDC7', command=entry_velocidad)
btn_t = Button(ventana, text='Tiempo total', bg='#DFDDC7', command=entry_tiempo)

# UBICACION BOTONES MAIN
btn_bg.place(x=15, y=255, width=346, height=430)
btn_pos.place(x=25, y=265, width=326, height=25)
btn_v.place(x=25, y=295, width=326, height=25)
btn_t.place(x=25, y=325, width=326, height=25)

# MAIN GRAFICOS / DATOS
header_animado = Frame(bg='#A34A28')
graph_body1 = Frame(ventana, bg='#A34A28')
graph_body2 = Frame(ventana, bg='#A34A28')
graph_datos1 = Label(ventana, text=var_mru[1]['defi_grafico_posicion'], bg='#C38154', fg='#fff')
graph_datos2 = Label(ventana, text=var_mru[1]['defi_grafico_velocidad'], bg='#C38154', fg='#fff')
vel_anima = Label(ventana, text='INGRESA DATOS',bg='#DFDDC7', fg='#000')

# UBICACION MAIN GRAFICOS / DATOS
header_animado.place(x=386, y=5, width=888, height=150)
graph_body1.place(x=386, y=171, width=442, height=524)
graph_body2.place(x=833, y=171, width=442, height=524)
graph_datos1.place(x=391, y=476, width=432, height=150)
graph_datos2.place(x=838, y=476, width=432, height=150)
vel_anima.place(x=1095, y=10, width=174, height=140)

# GRAFICOS
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
    ax1.set(xlabel='Tiempo (s)', ylabel='Posición (m)')
    ax1.grid(color='black', linestyle='--', linewidth=0.5)
    fig1.tight_layout()

    ax2.set_title('Grafico Velocidad - Tiempo')
    ax2.set(xlabel='Tiempo (s))', ylabel='Velocidad (m/s)')
    ax2.grid(color='black', linestyle='--', linewidth=0.5)
    fig2.tight_layout()

    canvas1 = FigureCanvasTkAgg(fig1, master=ventana)
    canvas2 = FigureCanvasTkAgg(fig2, master=ventana)

    canvas1.draw()
    canvas2.draw()
    canvas1.get_tk_widget().place(x=391, y=176)
    canvas2.get_tk_widget().place(x=838, y=176)
graficos("")
animacion("")
ventana.mainloop()