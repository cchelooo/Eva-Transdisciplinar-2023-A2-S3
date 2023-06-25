import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# Variables globales
velocidad = 0
tiempo = 0
distancia = 0

tiempo_grafico = [0, 0]
posicion_grafico = [0, 0]

ventana = tk.Tk()                                                              # creación de la ventana 
ventana.title('Movimiento uniforme rectilineo (MUR)')                          # titulo de la ventana
ventana.geometry("1280x700")                                                   # Tamaño de la ventana
ventana.resizable(False, False)                                                # para que el usuario no cambie el tamaño de la ventana
ventana.configure(bg='#2F4F52')                                                # color de fondo de la ventana
#   --------------------- Fondo 1/4 de la pantalla en x 
fondo1 = Frame(ventana, bg= "#253D40")
fondo1.place(x = 0, y = 0, width= 375 , height= 700)

fondo2 = Frame(ventana, bg= "#396063")
fondo2.place(x = 5, y = 5, width= 360 , height= 690)
#  ------------------------ Fondo de animacion -----------------
fondo3 = Frame(ventana,bg = "#48A683")
fondo3.place(x = 390 , y = 5, width= 870, height= 80)
fondo4 = Frame(ventana, bg = "#088556")
fondo4.place(x = 390, y = 85,  width= 870, height= 20)
#  --------------------------- linia de separacion ---------------------
dodo = Frame(ventana, bg="#132B22")
dodo.place( x = 820 , y = 105, width= 5, height= 590)
#   -------------------- Fondo decoración ----------------------
fondo3 = Frame(ventana,bg = "#367867")
fondo3.place(x =  400, y = 155, width= 405, height= 270)
fondo4 = Frame(ventana, bg = "#367867")
fondo4.place(x = 840, y = 155 ,  width= 400, height= 270)
#   -------------------- Fondo descripcion del graficos pos ----------------------
fondo5 = Frame(ventana,bg = "#48A683")
fondo5.place(x =  500, y = 160, width= 300, height= 250)
fondo6 = Frame(ventana, bg = "#48A683")
fondo6.place(x = 845, y = 160 ,  width= 300, height= 250)
# -------------------------Fondo para texto----
fondo7 = Frame(ventana,bg = "#396063")
fondo7.place(x =  400, y = 440, width= 400, height= 150)
fondo8 = Frame(ventana, bg = "#396063")
fondo8.place(x = 840, y = 440 ,  width= 400, height= 150)
#   --------------------- Fondo de pos grafico ---------------------
#fondo3 = Frame(ventana,bg = "#306E57")
#fondo3.place(x =  590, y = 145, width= 340, height= 260)
#fondo4 = Frame(ventana, bg = "#306E57")
#fondo4.place(x = 590, y = 418 ,  width= 340, height= 260)


definicion_mru = ''' El mru es.... 
.........texto..........
.........texto..........
.........texto..........
.........texto..........
.........texto..........
.........texto..........
'''

fig1 = plt.figure(figsize=(6, 4), dpi=100)
ax1 = fig1.add_subplot(111)
ax1.plot()
ax1.set(xlim=[0, 100], ylim=[0, 100], xlabel='X', ylabel='Y')
ax1.grid(color='black', linestyle='--', linewidth=0.5)

canvas1 = FigureCanvasTkAgg(fig1, master=fondo6)
canvas1.draw()
canvas1.get_tk_widget().place(x=0, y=0, width=300, height=250)


fig = plt.figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot()
ax.set(xlim=[0, 100], ylim=[0, 100], xlabel='X', ylabel='Y')
ax.grid(color='black', linestyle='--', linewidth=0.5)

canvas = FigureCanvasTkAgg(fig, master=fondo5)
canvas.draw()
canvas.get_tk_widget().place(x=0, y=0, width=300, height=250)

#----------------------------mini ventana-----------
def mini_ventana():
    global definicion_mru    # llama el texto que estaba externo
    window = tk.Toplevel(ventana)   #  # crear una ventanan la parte superior de todas las demas ventanas. 
    window.geometry("750x500") # las dimensiones de la ventana
    window.configure(bg="grey") # usamos un método de configuracion, en bg = "grey" , pintara el fondo de gris

    tit1 = Label(window, text="El movimiento rectilíneo uniforme", fg = "white", bg = "grey")  # la creación del titulo ,en window, con el color de letra blanca , y el mimo color de fondo (gris)
    definicion = tk.Label(window, text= definicion_mru,fg = "white", bg = "grey") # creacion del texto, en window,en text colocara el str que este en la variable definicion_mru , color de fondo blanco
    i = PhotoImage(file = "img01.png")   # usamos la clase PhotoImage para agregamos la imagen , y file para especificar que imagen
    imagen_pinta = Label(window, image = i) # luego en una varibale, se crea widget Label, en cual se le pasa la i en un armento imagen(los que nos permitira que se muestre en ventana la imagen)
#    imagen_pinta.image = i   # usar en caso que se tenga mas imagenes en este caso no ya que hay una nomasn (funcion de la linia = mostrar ciertas imagenes)
    imagen_pinta.configure(bg="grey") # colocar el fondo gris

    tit1.pack(padx = 20, pady= 10, ipadx = 30 , ipady = 3)  # (titulo) mostrar en la pantalla con las cordenas y tamaños indicados
    imagen_pinta.pack(padx= 20, pady = 20, ipadx= 500 , ipady = 20)   #(imagen) mostrar en la pantalla con las cordenas y tamaños indicados
    definicion.pack(padx = 20, pady= 20, ipadx = 400 , ipady = 200)   #(texto = definicion ) mostrar en la pantalla con las cordenas y tamaños indicados
    window.mainloop()  # ejecutar y mostrar en pantalla los contenidos de la mini ventana

#------------varibles con textos(definición de velocidad,posicion, distancia)----------------------------------------------
defi_velocidad = """La velocidad es write_write_write_write
y tiene como unidad de mmedida km/h o m/s write
y esta se calcula , como write_write_write_writ
w_write_write_write_write_write_write_write_wri
write_write.write.write.write.write.write.write.
write.write.write.write.write.write.write.write.
write.write.write.write.write.write.write.write."""

defi_posicion = """La posicion es write.write.write.write.write.wr
tiene como unidad de media m, km , etc, y write.
se calcula como write.write.write.write.write.w
write.write.write.write.write.write.write.write.
write.write.write.write.write.write.write.write.
write.write.write.write.write.write.write.write."""

defi_tiempo = """El tiempo es write.write.write.write.write.writ
y du unidad SI es s , h , etc write.write.write.
y se calcula como write.write.write.write.write.
write.write.write.write.write.write.write.write.
write.write.write.write.write.write.write.write.
write.write.write.write.write.write.write.write."""
# -- textos de las descripcion de los graficos ------------- ( posible cambio)/ o elmine por la agregar datos cada vez se opere uno nuevo
defi_grafico_velocidad = '''
Como se puede obsebar en el grafico , encontramos
 x(posicion) en el eje y ,t(tiempo) en el eje x ,
 en que tiene una pendiente creciente la cual esta indica 
la.......................................................
el grafico en si esta mostrando el.......................
y esto ..................................................
'''
defi_grafico_posicioon = '''
Como se puede obsebar en el grafico , encontramos 
x(posicion) en el eje y ,t(tiempo) en el eje x ,en 
que tiene una pendiente creciente la cual esta indica 
la.......................................................
el grafico en si esta mostrando el.......................
y esto ..................................................
'''
defi_grafico_tiempo = '''
Como se puede obsebar en el grafico , encontramos
x(posicion) en el eje y ,t(tiempo) en el eje x ,en que 
tiene una pendiente creciente la cual esta indica 
la.......................................................
el grafico en si esta mostrando el.......................
y esto ..................................................
'''
# -------------------objetos en ventana---------------------------------------
Bienvenida = Label(ventana, text = "Bienvenido a la aplicación <<<-MRU->>> ",fg="white", bg='#396063', font=("Arial", 13))
definicion = """
El movimiento rectilino uniforme, es el movimiento de 
un objeto, que viaja en una tayectoria de linia recta
con velocidad constante"""
texto1 = Label(ventana,text = definicion,bg = "#367867",fg = "white")

def b_velocidad():
#   ---------------------2 mini mapa -----------  # Este mapa explica com se hizo los calculos
    def explicacion_mini_window1():
        ventana = tk.Toplevel()
        ventana.title('Movimiento uniforme rectilineo (MUR)')
        ventana.geometry("462x500")
        ventana.resizable(False, False)
        ventana.configure(bg='#0C362A')
#       -------------- datos---------------------------
        a = caja1.get()      # Usamos la función get , para obtener el dato que tiene la caja 1 y se guarda en una variable llamada "a"
        b = caja2.get()      # Usamos la función get , para obtener el dato en caja 2 y se almacena en "b"
        c = caja3.get()      # Usamos la función get , para obtener el dato en caja 3 y se almacena en "c"
        d = caja4.get()      # Usamos la función get , para obtener el dato en caja 4 y se almacena en "d"
        decimal = round(((float(b) - float(a) )/(float(d)-float(c))), 10)   # Ocupamos los datos a,b,c,d, lo convertimos en float y operamos
        resta1 = float(b)-float(a)                                          # ocupamos a,b , la operación resta que de se guarda en "resta1"
        resta2 = float(d)-float(c)                                          # ocupamos a,b , la operación resta que de se guarda en "resta1"
        linia = "_"*20 # Posible modificacion (la linia tiene que ser determinada por cuantos nuemros hay)
#       ------------------Variables con textos--------------------------------------
        paso1= "Posición Final:       xf = {} m\t\tTiempo Final:       tf = {} s\nPosición Inicial:     xi = {} m\t\tTiempo Inicial:     ti = {} s".format(b,d,a,c)
        paso2= "\t{} m - {} m\n v = \t{} \n\t{} s - {} s".format(b,a,linia,d,c)
        paso3= "\t{}\nv = \t{} m \n\t{} s" .format(resta1,linia,resta2)
        paso4= "v =\t{} m/s\n".format(decimal)
#       ------------------Fondo de mini window1---------------------------------------
        Fondo_c_1 = Frame(ventana, bg = "#0E3D30")
        Fondo_c_1.place(x = 5, y = 5, width= 450, height= 260)
        Fondo_c_2 = Frame(ventana,bg = "#155C48")
        Fondo_c_2.place(x= 5, y = 145,width= 450, height= 350)
#       -------Creación de los objetos de textos con la class Label, estos incluyen fondo , color de letra, fuente de letra --------------------------------------
        titulo = Label(ventana, text = "¿Comó se calculo?", bg = "#0E3D30", fg = "white", font= ("Bonodi", 13,"bold italic")) 
        subtitulo = Label(ventana,text = "Para poder sacar la Velocidad constante \n usamos esta ecuación ---->",bg = "#0E3D30", fg = "white", font= ("Bonodi", 8,"bold italic"))
        Definicion = Label(ventana, text = "'Donde La velocidad es igual a la diferencia entre la posición final(xf) y la posición \ninicial(xi) dividido por la diferencia entre el tiempo \nfinal(tf) y el tiempo inicial(ti).'",bg = "#0E3D30", fg = "white", font= ("Bonodi", 8,"italic"))
        datos = Label(ventana, text="Los datos que se ingresaran en la ecuación:",bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
        datos2 = Label(ventana, text= paso1,bg= "#155C48",fg= "white",font= ("Bodoni", 8,"italic"))
        texto3 = Label(ventana, text = "Remplazamos los datos:",bg= "#155C48",fg= "white",font= ("Bodoni", 8,"bold italic"))
        texto3_1 = Label(ventana, text=paso2,font= ("Bodoni MT",10,"italic"))
        texto4 = Label(ventana,text= "Restamos la posiciones xf y xi para encontrar la distancia recorrida y \nrestamos el tf y ti para encontrar el tiempo total",bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
        texto4_1 = Label(ventana, text = paso3,font= ("Bodoni MT",10,"italic"))
        texto5 = Label(ventana,text = "Finalmente dividimos la distancia total recorrida con el tiempo total",bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
        texto6 = Label(ventana,text = paso4,font= ("Bodoni MT",10,"italic"))
        texto7 = Label(ventana,text= "Dandonos como resultado final {} metros por segundo".format(decimal),bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
#       --------------- imagenes importadas --------------------------------
        imagen_velocidad = PhotoImage(file = "F04.png")  
        imag_v = Label(ventana, image = imagen_velocidad) 
        imag_v.image = imagen_velocidad
#       ---------------Cordenadas del eje X y eje Y donde se posicionar los objetos-------------------------
        titulo.place(x = 10, y = 10)                    
        subtitulo.place( x = 10 , y = 40)               
        imag_v.place(x=280, y = 35 )                    
        Definicion.place(x = 10, y = 90)                
        datos.place(x = 10, y = 150)
        datos2.place(x = 15, y = 180)
        texto3.place(x = 10, y = 220)
        texto3_1.place(x = 150, y = 248)
        texto4.place(x = 10, y= 310)
        texto4_1.place(x= 150,y = 355)
        texto5.place(x = 10, y = 415)
        texto6.place(x = 150, y = 445,height=25)    # Este objeto se posiciona en eje x = 150, eje y = 445 y tendra una altura de 25
        texto7.place(x= 10, y = 475)
#   ------------Calculo de velocida-----------
    def BOTON():
        global Pi,Pf,Ti,Tf
        a = caja1.get()    # Usamos la función .get(), para obtener el dato en caja 1 , y se almacena en "a"
        b = caja2.get()    # obtenemos el dato en caja2, se guarda en "b"
        c = caja3.get()    # obtenemos el dato en caja2, se guarda en "b"
        d = caja4.get()    # obtenemos el dato en caja2, se guarda en "b"
#       ----------------------------------------------------------------
        calcular = round(((float(b) - float(a) )/(float(d)-float(c))),6)   
        velocidad = "La velocidad constante es " + str(calcular) + " m/s "
        Pi = float(a)
        Pf = float(b)
        Ti=float(c)
        Tf=float(d)
        grafico_velocidad()

        c_res1 = Label(ventana, text= velocidad,fg = "white", bg = "#367867")
        b_explica_cal = Button(ventana, text = " ¿Comó se calculo ? | (Haga clic Aqui)", bg = "#253D40",fg= "white", command = explicacion_mini_window1)
        c_res1.place(x = 40, y = 560 ,width = 280, height= 20)
        b_explica_cal.place(x = 20 , y = 580, width= 320, height= 30)


#  --------------------Creacion del los objetos en el cuadro 4 --------------------------------------
        titulo_cuadro4 = Label(ventana, text= "Explicacion del gráfico: ",bg = "grey")                                                # texto que sera el titulo, con fondo gris
        explicacion_grafico = Label(ventana, text = defi_grafico_posicioon)                                                           # texto que tendra la definicion
        Preg_1 = Label(ventana, text = "¿Desea saber como se ve el grafico\n velocidad y aceleracion?", fg = "white", bg = "grey")    # texto , color de letra blanco y fondo gris
        B_Preg_1 = Button(ventana, text = "Presiones Aquí", fg = "white", bg= "#367867")                                              # boton , color de letra blanco , color de fondo celeste
#   -----------Cordenas de hubicacion de los objetos del cuadro 4--------------
        titulo_cuadro4.place(x = 920, y = 310, width= 330, height=30)                     # cordenas de donde se hubicara y tamaño(ancho y altura)
        explicacion_grafico.place(x = 920, y = 340,width= 330, height = 200)              # cordenas de donde se hubicara y tamaño(ancho y altura)
        Preg_1.place(x = 920, y = 540,width= 330, height = 30)                            # cordenas de donde se hubicara y tamaño(ancho y altura)
        B_Preg_1.place(x = 920, y = 571,width= 330, height = 30)                          # cordenas de donde se hubicara y tamaño(ancho y altura)
#   ------------- Creacion del fondo---------------------------------------
    Fondo = Frame(ventana,bg = '#367867')
    Fondo.place(x = 20,y = 380 , width= 320, height= 230)
#   --------------Creacion de los objetos usando class (Label,Entry y Button)---------------------------------------------
    solicitud = Label(ventana, text = "Ingrese los siguientes datos: ", bg='#367867', fg= "white",font= ("Arial",13))   
    xi = Label(ventana, text= "Ingrese posicion inicial en m:",fg= "white", bg="#367867")
    xf = Label(ventana, text= "Ingrese posicion final en m:",fg= "white", bg="#367867")   
    ti = Label(ventana, text= "Ingrese tiempo inicial en s :", fg= "white",bg="#367867")
    tf = Label(ventana, text= "Ingrese tiempo final en s :", fg= "white",bg="#367867")
    caja1 = Entry(ventana)
    caja2 = Entry(ventana)
    caja3 = Entry(ventana)
    caja4 = Entry(ventana)
    Bot_C = Button(ventana,text="Calcular",bg='grey',command=BOTON)
#   ------------Cordenadas de los objetos en eje X y eje Y---------------------------
    solicitud.place(x = 70 , y =  385)
    xi.place(x = 30 , y =  415)
    xf.place(x = 30 , y =  445)
    ti.place(x = 30, y = 475)
    tf.place(x = 30, y = 505)
    caja1.place(x = 220 , y =  415,width= 100)    # Posicion en eje x , eje y , y la longitud del objeto
    caja2.place(x = 220 , y =  445,width= 100)    # Posicion en eje x , eje y , y la longitud del objeto
    caja3.place(x = 220, y = 475,width= 100)      # Posicion en eje x , eje y , y la longitud del objeto
    caja4.place(x= 220,y = 505,width= 100)        # Posicion en eje x , eje y , y la longitud del objeto
    Bot_C.place(x = 30 , y =  530)
#   ------------Texto que se cambia ------------------------------
    texto1.configure(text=defi_velocidad)  # este cambia el texto actual por uno nuevo


def b_distancia():
    def explicacion_mini_window2():
        ventana = tk.Toplevel()
        ventana.title('Movimiento uniforme rectilineo (MUR)')
        ventana.geometry("435x365")
        ventana.resizable(False, False)
        ventana.configure(bg='#0C362A')
#       --------------Datos---------------------------
        a = caja1.get()                               # Usamos la función get , para obtener el dato en caja 1 y se almacena en "a"
        b = caja2.get()                               # Usamos la función get , para obtener el dato en caja 2 y se almacena en "b"
        calcular = float(a) * float(b)                # utilizamos los datos a,b, se convierte en float , y la operación que de se guarda en "calcular"
#       --------------Variables con textos-------------------------------------------
        paso1= "Velocidad Constante:     {}\nTimpo Total:    {}".format(a,b)
        paso2= "d =\t{} m/s x {} s".format(a,b)
        paso3= "d =\t{} m".format(calcular)
#       ---------------Fondo----------------------------------------
        Fondo_c_1 = Frame(ventana, bg = "#0E3D30")
        Fondo_c_1.place(x = 5, y = 5, width= 425, height= 260)
        Fondo_c_2 = Frame(ventana,bg = "#155C48")
        Fondo_c_2.place(x= 5, y = 145,width= 425, height= 215)
#       --------------Creación de los objetos de textos, estos incluyen fondo , color de letra, fuente de letra-----------------------------
        titulo = Label(ventana, text = "¿Comó se calculo?", bg = "#0E3D30", fg = "white", font= ("Bonodi", 13,"bold italic")) 
        subtitulo = Label(ventana,text = "Para poder sacar la Distancia Recorrida \n usamos esta ecuación ---->",bg = "#0E3D30", fg = "white", font= ("Bonodi", 8,"bold italic"))
        Definicion = Label(ventana, text = "'Donde la distancia recorrida es igual a la mutiplicación entre la \nvelocidad constante y timpo total'",bg = "#0E3D30", fg = "white", font= ("Bonodi", 8,"italic"))
        datos = Label(ventana, text="Los datos que se ingresaran en la ecuación:",bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
        datos2 = Label(ventana, text= paso1,bg= "#155C48",fg= "white",font= ("Bodoni", 8,"italic"))
        texto3 = Label(ventana, text = "Remplazamos los datos y multiplicamos",bg= "#155C48",fg= "white",font= ("Bodoni", 8,"bold italic"))
        texto3_1 = Label(ventana, text=paso2,font= ("Bodoni MT",12,"italic"))
        texto4 = Label(ventana,text= "Al multiplicar nos da :",bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
        texto4_1 = Label(ventana, text = paso3,font= ("Bodoni MT",12,"italic"))
        texto5 = Label(ventana,text = "Dandonos como resultado que la distancias recorrida es {} metros ".format(calcular),bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
#       --------------- imagenes importadas ------------------------------
        imagen_posicion_distancia = PhotoImage(file = "f_D01.png")
        imag_p_d = Label(ventana, image = imagen_posicion_distancia)
        imag_p_d.image = imagen_posicion_distancia 
#       -------------------Posiciones de los objetos-------------------------
        titulo.place(x = 10, y = 10)
        subtitulo.place( x = 10 , y = 40)
        imag_p_d.place(x=280, y = 35 )
        Definicion.place(x = 10, y = 90)
        datos.place(x = 10, y = 150)
        datos2.place(x = 15, y = 180)
        texto3.place(x = 10, y = 220)
        texto3_1.place(x = 150, y = 248)
        texto4.place(x = 10, y= 288)
        texto4_1.place(x= 150,y = 310)
        texto5.place(x = 10, y = 340)
#   ---------------Calculo de distancia----------------------------
    def BOTON():
        a = caja1.get() 
        b = caja2.get() 
        calcular = float(a) * float(b)
        velocidad = "La distancia recorrida es " +str(calcular) + " metros"
#       ------------------------------------------------
        c_res1 = Label(ventana, text= velocidad,fg = "white", bg = "#367867")
        b_explica_cal = Button(ventana, text = " ¿Comó se calculo ? | (Haga clic Aqui)", bg = "#253D40",fg= "white", command = explicacion_mini_window2)
        c_res1.place(x = 40, y = 525 ,width = 280, height= 20)
        b_explica_cal.place(x = 20 , y = 545, width= 320, height= 30)


#  --------------------Creacion del los objeto del cuadro 4 --------------------------------------
        titulo_cuadro4 = Label(ventana, text= "Explicacion del gráfico: ",bg = "grey")                                              # texto que sera el titulo, con fondo gris
        explicacion_grafico = Label(ventana, text = defi_grafico_posicioon)                                                         # texto que tendra la definicion
        Preg_1 = Label(ventana, text = "¿Desea saber como se ve el grafico\n velocidad y aceleracion?", fg = "white", bg = "grey")  # texto , color de letra blanco y fondo gris
        B_Preg_1 = Button(ventana, text = "Presiones Aquí", fg = "white", bg= "#367867")           # boton , color de letra blanco , color de fondo celeste
#           -----------Cordenas de hubicacion de los objetos del cuadro 4--------------
        titulo_cuadro4.place(x = 920, y = 310, width= 330, height=30)             # cordenas de donde se hubicara y tamaño(ancho y altura)
        explicacion_grafico.place(x = 920, y = 340,width= 330, height = 200)      # cordenas de donde se hubicara y tamaño(ancho y altura)
        Preg_1.place(x = 920, y = 540,width= 330, height = 30)                    # cordenas de donde se hubicara y tamaño(ancho y altura)
        B_Preg_1.place(x = 920, y = 571,width= 330, height = 30)                  # cordenas de donde se hubicara y tamaño(ancho y altura)
#   ---------------- Fondo ----------
    Fondo = Frame(ventana, bg = "#367867")
    Fondo.place(x = 20 , y = 380, width= 320, height= 230)
#   -----------Creacion de los objetos------------------------
    solicitud = Label(ventana, text = "Ingrese los siguientes datos: ", bg="#367867", fg= "white",font=("Arial",13))
    v = Label(ventana, text= "Ingrese velocidad m/s:",fg= "white", bg= "#367867")
    t = Label(ventana, text= "Ingrese tiempo en s:", fg= "white",bg="#367867")
    caja1 = Entry(ventana)
    caja2 = Entry(ventana)
    Bot_C = Button(ventana,text= "Calcular",bg= 'grey',command= BOTON)
#    ----------Cordenas de los objetos------------------------
    solicitud.place(x = 70 , y =  384)
    v.place(x = 30 , y =  415)
    t.place(x = 30 , y =  445)
    caja1.place(x = 220 , y =  415, width= 100)
    caja2.place(x = 220 , y =  445, width= 100)
    Bot_C.place(x = 40 , y =  485)
#   -------------Texto que cambia ----------------------------
    texto1.configure(text = defi_posicion)  # este cambia el texto actual por uno nuevo


def b_tiempo():

    def explicacion_mini_window3():
        ventana = tk.Toplevel()
        ventana.title('Movimiento uniforme rectilineo (MUR)')
        ventana.geometry("415x455")
        ventana.resizable(False, False)
        ventana.configure(bg='#0C362A')
#       --------------_ Datos---------------------------
        a = caja1.get()                               # Usamos la función get, para obtener el dato en caja 1 y se almacena en "a"     
        b = caja2.get()                               # Usamos la función get, para obtener el dato en caja 2 y se almacena en "b"
        calcular = float(a) / float(b)       
        linia = "_"*20
#       ----------------Variables con texto----------------------------------
        paso1= "Distancia total recorrida:    {} m\nVelocidad constante:   {} m/s".format(a,b)
        paso2= "\t{} m\n t = \t{} \n\t{} m/s".format(a,linia,b)
        paso3= "t =\t{} s" .format(calcular)
#       ----------------Fondo--------------------------------------
        Fondo_c_1 = Frame(ventana, bg = "#0E3D30")
        Fondo_c_1.place(x = 5, y = 5, width= 405, height= 260)
        Fondo_c_2 = Frame(ventana,bg = "#155C48")
        Fondo_c_2.place(x= 5, y = 145,width= 405, height= 300)
#       -----------------------------------------------------------------------------------
        titulo = Label(ventana, text = "¿Comó se calculo?", bg = "#0E3D30", fg = "white", font= ("Bonodi", 13,"bold italic")) 
        subtitulo = Label(ventana,text = "Para poder sacar el Tiempo total \n usamos esta ecuación ---->",bg = "#0E3D30", fg = "white", font= ("Bonodi", 8,"bold italic"))
        Definicion = Label(ventana, text = "'Donde el tiempo es igual a la dividición entre la distancia total recorrida\ny velocidad constante.'",bg = "#0E3D30", fg = "white", font= ("Bonodi", 8,"italic"))
        datos = Label(ventana, text="Los datos que se ingresaran en la ecuación:",bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
        datos2 = Label(ventana, text= paso1,bg= "#155C48",fg= "white",font= ("Bodoni", 8,"italic"))
        texto3 = Label(ventana, text = "Remplazamos los datos :",bg= "#155C48",fg= "white",font= ("Bodoni", 8,"bold italic"))
        texto3_1 = Label(ventana, text=paso2,font= ("Bodoni MT",10,"italic"))
        texto4 = Label(ventana,text= "Al dvidir nos da como resultado ",bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
        texto4_1 = Label(ventana, text = paso3,font= ("Bodoni MT",10,"italic"))
        texto5 = Label(ventana,text = "Dandonos que el tiempo toal es {} segundos".format(calcular),bg = "#155C48", fg = "white", font= ("Bonodi", 8,"bold italic"))
#       ---------------imagenes importadas --------------------------------
        imagen_tiempo= PhotoImage(file = "f_T01.png") 
        imag_t = Label(ventana, image = imagen_tiempo)
        imag_t.image = imagen_tiempo
#       ---------------Posiciones de los objetos-------------------------
        titulo.place(x = 10, y = 10)
        subtitulo.place( x = 10 , y = 40)
        imag_t.place(x=280, y = 35 )
        Definicion.place(x = 10, y = 90)
        datos.place(x = 10, y = 150)
        datos2.place(x = 15, y = 180)
        texto3.place(x = 10, y = 220)
        texto3_1.place(x = 150, y = 248)
        texto4.place(x = 10, y= 310)
        texto4_1.place(x= 150,y = 355)
        texto5.place(x = 10, y = 415)
#   ---------------Calculo de tiempo------------------------
    def BOTON():
        a = caja1.get()                      # guarda el numero ingresado en Entry de velocidad 
        b = caja2.get()                      # guarda el numero ingresado en Entry de distancia 
        calcular = float(a) / float(b)       # convierte en float, opera la divición de los num guardados en la variable a y b , y los guarda en una varriable 
        velocidad = " El tiempo es " + str(calcular) + " segundos"  # Convierte el dato que esta en "calcular" y le agrega un str metros, la variable "velocidad "guarda un string
#       ------------------Objetos(texto y boton)----------------------------------
        c_res1 = Label(ventana, text= velocidad,fg = "white", bg = "#367867")
        b_explica_cal = Button(ventana, text = " ¿Comó se calculo ? | (Haga clic Aqui)", bg = "#253D40",fg= "white", command = explicacion_mini_window3)
        c_res1.place(x = 40, y = 525 ,width = 280, height= 20)
        b_explica_cal.place(x = 20 , y = 545, width= 320, height= 30)

#    ----------Creacion del los objetos en el cuadro 4 ------------------------
        titulo_cuadro4 = Label(ventana, text= "Explicacion del gráfico: ",bg = "grey")
        explicacion_grafico = Label(ventana, text = defi_grafico_posicioon)
        Preg_1 = Label(ventana, text = "¿Desea saber como se ve el grafico\n velocidad y aceleracion?", fg = "white", bg = "grey")
        B_Preg_1 = Button(ventana, text = "Presiones Aquí", fg = "white", bg= "#367867")
#   -----------Cordenas de hubicacion de los objetos del cuadro 4--------------        
        titulo_cuadro4.place(x = 920, y = 310, width= 330, height=30)
        explicacion_grafico.place(x = 920, y = 340,width= 330, height = 200)
        Preg_1.place(x = 920, y = 540,width= 330, height = 30)
        B_Preg_1.place(x = 920, y = 571,width= 330, height = 30)
#   ------------Fondo ---------------------------------------
    Fondo = Frame(ventana, bg = "#367867")
    Fondo.place(x = 20, y = 380, width= 320, height= 230)

#   -----------Creacion de los objetos--------------------
    solicitud = Label(ventana, text = "Ingrese los siguientes datos: ", bg='#367867', fg= "white",font=("Arial",13))
    v = Label(ventana, text= "Ingrese distancia en m :",fg= "white", bg='#367867')
    d = Label(ventana, text= "Ingrese velocidad m/s :", fg= "white",bg='#367867')
    caja1 = Entry(ventana)
    caja2 = Entry(ventana)
    Bot_C = Button(ventana,text= "Calcular",bg= 'grey',command= BOTON)
#    ----------Cordenas de los objetos------------------
    solicitud.place(x = 70, y =  385)
    v.place(x = 30 , y =  415)
    d.place(x = 30 , y =  445)
    caja1.place(x = 220 , y =  415, width= 100)
    caja2.place(x = 220 , y =  445, width= 100)
    Bot_C.place(x = 40 , y =  485)
#   -------------Texto se cambia ------------------------
    texto1.configure(text=defi_tiempo) # este cambia el texto actual por uno nuevo


def grafico_velocidad():
    global velocidad, tiempo, ventana,ax1,canvas1,distancia

    # Crear y mostrar gráfico de posición-tiempo
    tiempo_grafico = [0, tiempo]
    posicion_grafico = [0, distancia]

    ax1.clear()
    ax1.grid(color="blue", linestyle='--', linewidth=0.5)
    ax1.plot(tiempo_grafico, posicion_grafico)
    ax1.set_xlabel('Tiempo (s)')
    ax1.set_ylabel('Posición (m)')
    ax1.set_title('Gráfico de Posición vs Tiempo')

        # Dibujar línea horizontal en la posición actual
    ax1.axhline(y=posicion_grafico[1], color='red', linestyle='--')

    tiempo = Tf - Ti
    posicion = velocidad * tiempo

    # Iterar sobre los puntos y mostrarlos en el gráfico
    for i in range(1, len(tiempo_grafico)):
        ax1.plot(tiempo_grafico[i-1:i+1], posicion_grafico[i-1:i+1], 'ro')  # Punto actual en rojo
        plt.plot([tiempo, tiempo+1], [posicion, posicion+velocidad], 'b-') # Línea entre puntos en azul

    canvas1.draw()

#-------------- Creacion de los objetos, que se mostraran en pantalla/ventana (button and Label)----------------------------

boton_infor = Button(ventana,text = "Mas informacion....",bg= "grey",command= mini_ventana) # creacion del botton infomativo , se mostrara en ventana, con un texto ,fondo gris, y un comando que al precionarlo abrira una mini ventana
tex2 = Label(ventana,text= "¿ Qué desea calcular ?",bg='#396063', fg = "white", font=("Arial",11,))                 # creación de un texto, en ventana y fondo verde opaco 
boton1= Button(ventana,text="La Velocidad Constante", bg = "grey",command = b_velocidad)       # creación boton 1 , color de fondo gris , falta un command...
boton2 = Button(ventana,text="La Distancia recorrida", bg = "grey",command = b_distancia)     # creación boton 2 , color de fondo gris , falta un command...
boton3= Button(ventana,text="El Tiempo total", bg = "grey",command = b_tiempo)             # creación boton 3 , color de fondo gris , falta un command...

# ------------------- posciciones en la que se mostrara el objeto-------------------------------------

Bienvenida.place(x = 27,y = 20, width= 310, height=30) # cordenadas de donde se ubicara y tamaño
texto1.place(x = 20, y = 50, width= 300, height= 140) # cordenadas de donde se ubicara y tamaño 

tex2.place(x = 90,y = 210)                                     # cordenadas de donde se ubicara
boton1.place(x = 70 , y = 245, width = 200, height= 30)        # cordenadas de donde se ubicara 
boton2.place(x = 70, y = 277, width = 200, height= 30)         # cordenadas de donde se ubicara 
boton3.place(x = 70, y = 309,width = 200, height = 30)         # cordenadas de donde se ubicara 
boton_infor.place(x = 20, y = 660)                             # cordenadas de donde se ubicara 



ventana.mainloop() # ejecutar y mostrar en pantalla los contenidos de la ventana principal