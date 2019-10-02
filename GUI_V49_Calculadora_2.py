## GUI  - Video 49

#-- Importación de librerías
from tkinter import *

# Crea la  raíz (ventana principal)------------------------------------------------------------------
raiz  = Tk()
raiz.title(" ")
raiz.iconbitmap("Calculator.ico")

# Crea Frame-----------------------------------------------------------------------------------------
miFrame = Frame(raiz, width = 500, height = 400, bg = 'lightgray')
miFrame.pack()

#____________________________________________________________________________________________________
# VARIABLES

# Numeros
numeroPantalla = StringVar()

# Ancho y alto botones calculadora
widthButtom = 8  #Ancho
heigthButton = 2 #Alto

# Tamaño de fuente de pantalla
fontSizeDisp = 21

# PadX, PadY
padX = 5
padY = 5

# variable para operaciones
operacion = ""   # Al ejecutar el programa, el valor vale "vacío"
resultado = int(0)


#____________________________________________________________________________________________________
# FUNCIONES
 # Pulsación de teclado
def numeroPulsado(num):
    global operacion 
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)
    
# Operación de suma
def suma(num):
    global operacion     # traer la variable global "operación"
    global resultado     # almacena el resultado (temporal)
    operacion = "suma"
    
    resultado += int(num)    
    numeroPantalla.set(resultado)


# Función el_resultado (=)
def el_resultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0


#____________________________________________________________________________________________________

#-- CALCULADORA--------------------------------------------------------------------------------------

# Pantalla
pantalla = Entry(  miFrame
                 , textvariable = numeroPantalla
                 , font=('Ubuntu', fontSizeDisp)
                )

pantalla.config(bg = 'black', fg = '#03f943', justify = 'right')
pantalla.grid(row = 1, column = 1
              , padx = padY, pady = padY
              , columnspan = 4   # Amplia a 4 columnas
              )


#-----------------------------------------------------------------------------------------------------
#Fila 1
boton7 = Button(miFrame, padx = padX, pady = padY, text = '7', width = widthButtom, height = heigthButton, command = lambda:numeroPulsado('7')).grid(row = 2, column = 1)
boton8 = Button(miFrame, padx = padX, pady = padY, text = '8', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('8')).grid(row = 2, column = 2)
boton9 = Button(miFrame, padx = padX, pady = padY,text = '9', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('9')).grid(row = 2, column = 3)
botonDiv = Button(miFrame, padx = padX, pady = padY,text = '/', width = widthButtom, height = heigthButton,).grid(row = 2, column = 4)
#Fila 2
boton4 = Button(miFrame, padx = padX, pady = padY,text = '4', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('4')).grid(row = 3, column = 1)
boton5 = Button(miFrame,padx = padX, pady = padY, text = '5', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('5')).grid(row = 3, column = 2)
boton6 = Button(miFrame, padx = padX, pady = padY,text = '6', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('6')).grid(row = 3, column = 3)
botonMult = Button(miFrame, padx = padX, pady = padY,text = 'X', width = widthButtom, height = heigthButton).grid(row = 3, column = 4)
#Fila 3
boton1 = Button(miFrame, padx = padX, pady = padY,text = '1', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('1')).grid(row = 4, column = 1)
boton2 = Button(miFrame, padx = padX, pady = padY,text = '2', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('2')).grid(row = 4, column = 2)
boton3 = Button(miFrame, padx = padX, pady = padY,text = '3', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('3')).grid(row = 4, column = 3)
botonRest = Button(miFrame, padx = padX, pady = padY,text = '-', width = widthButtom,height = heigthButton).grid(row = 4, column = 4)
#Fila 4
boton0 = Button(miFrame, padx = padX, pady = padY,text = '0', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('0')).grid(row = 5, column = 1)
botonComa = Button(miFrame, padx = padX, pady = padY,text = '.', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('.')).grid(row = 5, column = 2)
botonIgual = Button(miFrame, padx = padX, pady = padY,text = '=', width = widthButtom,height = heigthButton, command = lambda: el_resultado()).grid(row = 5, column = 3)
botonSum = Button(miFrame, padx = padX, pady = padY,text = '+', width = widthButtom, height = heigthButton, command = lambda:suma(numeroPantalla.get())).grid(row = 5, column = 4)



# Mantiene la ventana abierta
raiz.mainloop()

