import tkinter as tk
from tkinter import *

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
fondo3 = Frame(ventana,bg = "#48A683")
fondo3.place(x =  500, y = 160, width= 300, height= 250)
fondo4 = Frame(ventana, bg = "#48A683")
fondo4.place(x = 845, y = 160 ,  width= 300, height= 250)
# -------------------------Fondo para texto----
fondo3 = Frame(ventana,bg = "#396063")
fondo3.place(x =  400, y = 440, width= 400, height= 150)
fondo4 = Frame(ventana, bg = "#396063")
fondo4.place(x = 840, y = 440 ,  width= 400, height= 150)
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
#-------------------------- preguntas en pantalla , ingresar dato--------------------
solicitud = Label(ventana, text = "Ingrese los siguientes datos: ", bg='#367867', fg= "white")

def b_velocidad():
#   ---------------------2 mini mapa -----------  # Este mapa explica com se hizo los calculos
    def explicacion_mini_window1():
        ventana = tk.Toplevel()
        ventana.title('Movimiento uniforme rectilineo (MUR)')
        ventana.geometry("460x260")
        ventana.resizable(False, False)
        ventana.configure(bg='#253D40')
        # -------------- texto en palabra ---------------------------
        texto_calculo = ''' 
        \t\ten la formula x  es :___________
        \t\ten el tiempo  t es :____________
        \t\ten velocidad v es:______________\n
        seguir explicando el calculo.................             
        write_write_write_write_write_write_write_write_write_write_w
        write_write_write_write_write_write_write_write_write_write_w
        '''
        #t_c3 = Label(ventana, text = Resultado_final )
        Resultado_final = "Como resultado final seria" + str('.tomar el resultado y colocarlo aca')
        # ----------------------------fondo y objetos----------------------------------------
        Fondo_c_3 = Frame(ventana, bg = "#367867")
        Fondo_c_3.place(x = 5, y = 5, width= 450, height= 250)
        titulo_cuadro3 = Label(ventana, text = "¿Comó se calculo?", bg = "#367867", fg = "white", font= ("Arial", 13) ) 
        texto_calculo1 = Label(ventana, text = texto_calculo, bg = "#367867", fg = "white")
        Resultado_final = Label(ventana,text= Resultado_final, bg = "#367867", fg = "black")
        #  --------------- imagenes importadas ------------------------------
        imagen_velocidad = PhotoImage(file = "F04.png")  
        #    ------------------------ la imagen en Label----------------
        imag_v = Label(ventana, image = imagen_velocidad) # imagen_pinta.image = i   # imagen_pinta.configure(bg="grey")
        imag_v.image = imagen_velocidad  
    #   ---------------posicion 
        titulo_cuadro3.place(x= 30, y = 10)
        texto_calculo1.place(x = 30, y = 40, width = 400, height= 130)
        imag_v.place(x = 32, y = 50)
        Resultado_final.place(x = 32,y =  200)
#   ------------Calculo de velocida-----------
    def BOTON():
        a = caja1.get() 
        b = caja2.get() 
        c = caja3.get()
        d = caja4.get()
#       ----------Fondo de los datos -----------------------------------
    #    Fondo2 = Frame(ventana, bg = "grey")
    #    Fondo2.place(x = 30 ,y = 560, width= 300, height= 25)
#       ----------------------------------------------------------------
        calcular = round(((float(b) - float(a) )/(float(d)-float(c))),6)
        velocidad = "La velocidad constante es " + str(calcular) + " m/s "

        c_res1 = Label(ventana, text= velocidad,fg = "white", bg = "#367867")
        b_explica_cal = Button(ventana, text = " ¿Comó se calculo ? | (Haga clic Aqui)", bg = "#253D40",fg= "white", command = explicacion_mini_window1)
        c_res1.place(x = 40, y = 560 ,width = 280, height= 20)
        b_explica_cal.place(x = 20 , y = 580, width= 320, height= 30)


#  --------------------Creacion del los objetos en el cuadro 4 --------------------------------------
        titulo_cuadro4 = Label(ventana, text= "Explicacion del gráfico: ",bg = "grey")                                                # texto que sera el titulo, con fondo gris
        explicacion_grafico = Label(ventana, text = defi_grafico_posicioon)                                                           # texto que tendra la definicion
        Preg_1 = Label(ventana, text = "¿Desea saber como se ve el grafico\n velocidad y aceleracion?", fg = "white", bg = "grey")    # texto , color de letra blanco y fondo gris
        B_Preg_1 = Button(ventana, text = "Presiones Aquí", fg = "white", bg= "#367867")                                                 # boton , color de letra blanco , color de fondo celeste
#           -----------Cordenas de hubicacion de los objetos del cuadro 4--------------
        titulo_cuadro4.place(x = 920, y = 310, width= 330, height=30)                     # cordenas de donde se hubicara y tamaño(ancho y altura)
        explicacion_grafico.place(x = 920, y = 340,width= 330, height = 200)              # cordenas de donde se hubicara y tamaño(ancho y altura)
        Preg_1.place(x = 920, y = 540,width= 330, height = 30)                            # cordenas de donde se hubicara y tamaño(ancho y altura)
        B_Preg_1.place(x = 920, y = 571,width= 330, height = 30)                          # cordenas de donde se hubicara y tamaño(ancho y altura)
#   ------------- Creacion del fondo.cuadrado 2---------------------------------------
    Fondo = Frame(ventana,bg = '#367867')
    Fondo.place(x = 20,y = 380 , width= 320, height= 230)
#   --------------Creacion de los objetos-------------------------------------------------------------------------
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
#   ------------Cordenadas de los objetos---------------------------
    solicitud.place(x = 70 , y =  385)
    xi.place(x = 30 , y =  415)
    xf.place(x = 30 , y =  445)
    ti.place(x = 30, y = 475)
    tf.place(x = 30, y = 505)
    caja1.place(x = 220 , y =  415,width= 100)
    caja2.place(x = 220 , y =  445,width= 100)
    caja3.place(x = 220, y = 475,width= 100)
    caja4.place(x= 220,y = 505,width= 100)
    Bot_C.place(x = 30 , y =  530)
#   ------------Texto que se cambia ------------------------------
    texto1.configure(text=defi_velocidad)  # este cambia el texto actual por uno nuevo


def b_distancia():
    def explicacion_mini_window2():
        ventana = tk.Toplevel()
        ventana.title('Movimiento uniforme rectilineo (MUR)')
        ventana.geometry("460x260")
        ventana.resizable(False, False)
        ventana.configure(bg='#253D40')
        # -------------- texto en palabra ---------------------------
        texto_calculo = ''' 
        \t\ten la formula x  es :___________
        \t\ten el tiempo  t es :____________
        \t\ten velocidad v es:______________\n
        seguir explicando el calculo.................             
        write_write_write_write_write_write_write_write_write_write_w
        write_write_write_write_write_write_write_write_write_write_w
        '''
        #t_c3 = Label(ventana, text = Resultado_final )
        Resultado_final = "Como resultado final seria" + str('.tomar el resultado y colocarlo aca')
        # ----------------------------fondo y objetos----------------------------------------
        Fondo_c_3 = Frame(ventana, bg = "#367867")
        Fondo_c_3.place(x = 5, y = 5, width= 450, height= 250)
        titulo_cuadro3 = Label(ventana, text = "¿Comó se calculo?", bg = "#367867", fg = "white", font= ("Arial", 13) ) 
        texto_calculo1 = Label(ventana, text = texto_calculo, bg = "#367867", fg = "white")
        Resultado_final = Label(ventana,text= Resultado_final, bg = "#367867", fg = "black")
        #  --------------- imagenes importadas ------------------------------
        imagen_posicion_distancia = PhotoImage(file = "f_D01.png")
        #    ------------------------ la imagen en Label----------------
        imag_p_d = Label(ventana, image = imagen_posicion_distancia)
        imag_p_d.image = imagen_posicion_distancia  
        #imag_v.configure(bg="#367867")

    #   -------------------------------------- posicion 
        titulo_cuadro3.place(x= 30, y = 10)
        texto_calculo1.place(x = 30, y = 40, width = 400, height= 130)
        imag_p_d.place(x = 32, y = 50)
        Resultado_final.place(x = 32,y =  200)
#   ---------------Calculo de distancia----------------------------
    def BOTON():
        a = caja1.get() 
        b = caja2.get() 
        calcular = float(a) * float(b)
        velocidad = "La distancia recorrida es " +str(calcular) + " metros"
#       ------------Fondo ------------------------------
#        Fondo2 = Frame(ventana, bg = "grey")
#        Fondo2.place(x = 30 ,y = 525, width= 300, height= 38)
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
        ventana.geometry("460x260")
        ventana.resizable(False, False)
        ventana.configure(bg='#253D40')
        # -------------- texto en palabra ---------------------------
        texto_calculo = ''' 
        \t\ten la formula x  es :___________
        \t\ten el tiempo  t es :____________
        \t\ten velocidad v es:______________\n
        seguir explicando el calculo.................             
        write_write_write_write_write_write_write_write_write_write_w
        write_write_write_write_write_write_write_write_write_write_w
        '''
        #t_c3 = Label(ventana, text = Resultado_final )
        Resultado_final = "Como resultado final seria" + str('.tomar el resultado y colocarlo aca')
        # ----------------------------fondo y objetos----------------------------------------
        Fondo_c_3 = Frame(ventana, bg = "#367867")
        Fondo_c_3.place(x = 5, y = 5, width= 450, height= 250)
        titulo_cuadro3 = Label(ventana, text = "¿Comó se calculo?", bg = "#367867", fg = "white", font= ("Arial", 13) ) 
        texto_calculo1 = Label(ventana, text = texto_calculo, bg = "#367867", fg = "white")
        Resultado_final = Label(ventana,text= Resultado_final, bg = "#367867", fg = "black")
        #  --------------- imagenes importadas ------------------------------
        imagen_tiempo= PhotoImage(file = "f_T01.png") 

        #    ------------------------ la imagen en Label----------------
        imag_t = Label(ventana, image = imagen_tiempo)
        imag_t.image = imagen_tiempo 
    #   -------------------------------------- posicion 
        titulo_cuadro3.place(x= 30, y = 10)
        texto_calculo1.place(x = 30, y = 40, width = 400, height= 130)
        imag_t.place(x = 32, y = 50)
        Resultado_final.place(x = 32,y =  200)
#   ---------------Calculo de tiempo------------------------
    def BOTON():
        a = caja1.get()                      # guarda el numero ingresado en Entry de velocidad 
        b = caja2.get()                      # guarda el numero ingresado en Entry de distancia 
        calcular = float(a) / float(b)       # convierte en float, opera la divición de los num guardados en la variable a y b , y los guarda en una varriable 
        velocidad = " El tiempo es " + str(calcular) + " segundos"  # Convierte el dato que esta en "calcular" y le agrega un str metros, la variable "velocidad "guarda un string
#       --------- Fondo ------------------------------------
#        Fondo2 = Frame(ventana, bg = "grey")
#        Fondo2.place(x = 30 ,y = 525, width= 300, height= 38)
#       ----------------------------------------------------
        c_res1 = Label(ventana, text= velocidad,fg = "white", bg = "#367867")
        b_explica_cal = Button(ventana, text = " ¿Comó se calculo ? | (Haga clic Aqui)", bg = "#253D40",fg= "white", command = explicacion_mini_window3)
        c_res1.place(x = 40, y = 525 ,width = 280, height= 20)
        b_explica_cal.place(x = 20 , y = 545, width= 320, height= 30)

#  --------------------Creacion del los objetos en el cuadro 4 --------------------------------------
        titulo_cuadro4 = Label(ventana, text= "Explicacion del gráfico: ",bg = "grey")
        explicacion_grafico = Label(ventana, text = defi_grafico_posicioon)
        Preg_1 = Label(ventana, text = "¿Desea saber como se ve el grafico\n velocidad y aceleracion?", fg = "white", bg = "grey")
        B_Preg_1 = Button(ventana, text = "Presiones Aquí", fg = "white", bg= "#367867")
#           -----------Cordenas de hubicacion de los objetos del cuadro 4--------------        
        titulo_cuadro4.place(x = 920, y = 310, width= 330, height=30)
        explicacion_grafico.place(x = 920, y = 340,width= 330, height = 200)
        Preg_1.place(x = 920, y = 540,width= 330, height = 30)
        B_Preg_1.place(x = 920, y = 571,width= 330, height = 30)
#   --------------------Fondo ----------------------------
    Fondo = Frame(ventana, bg = "#367867")
    Fondo.place(x = 20, y = 380, width= 320, height= 230)

#   ------------------Creacion de los objetos--------------------
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

#-------------- Creacion de los objetos, que se mostraran en pantalla/ventana (button and Label)----------------------------

boton_infor = Button(ventana,text = "Mas informacion....",bg= "grey",command= mini_ventana) # creacion del botton infomativo , se mostrara en ventana, con un texto ,fondo gris, y un comando que al precionarlo abrira una mini ventana
tex2 = Label(ventana,text= "¿ Qué desea calcular ?",bg='#396063') # creación de un texto, en ventana y fondo verde opaco 
boton1= Button(ventana,text="Velocidad", bg = "grey",command = b_velocidad)  # creación boton 1 , color de fondo gris , falta un command...
boton2 = Button(ventana,text="Distancia ", bg = "grey",command = b_distancia) # creación boton 2 , color de fondo gris , falta un command...
boton3= Button(ventana,text="Tiempo", bg = "grey",command = b_tiempo) # creación boton 3 , color de fondo gris , falta un command...

# ------------------- posciciones en la que se mostrara el objeto-------------------------------------

Bienvenida.place(x = 27,y = 20, width= 310, height=30) # cordenadas de donde se ubicara y tamaño
texto1.place(x = 20, y = 50, width= 300, height= 140) # cordenadas de donde se ubicara y tamaño 

tex2.place(x = 90,y = 210)    # cordenadas de donde se ubicara
boton1.place(x = 50 , y = 245, width = 200, height= 30)  # cordenadas de donde se ubicara 
boton2.place(x = 50, y = 277, width = 200, height= 30)  # cordenadas de donde se ubicara 
boton3.place(x = 50, y = 309,width = 200, height = 30)  # cordenadas de donde se ubicara 
boton_infor.place(x = 20, y = 660)  # cordenadas de donde se ubicara 



ventana.mainloop() # ejecutar y mostrar en pantalla los contenidos de la ventana principal