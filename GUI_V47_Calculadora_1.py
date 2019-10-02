## GUI  - Video 47

#-- Importación de librerías
from tkinter import *

# Crea la  raíz (ventana principal)------------------------------------------------------------------
raiz  = Tk()
raiz.title(" ")
raiz.iconbitmap("GUI\Calculator.ico")

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
#____________________________________________________________________________________________________
# FUNCIONES
def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)
    


#____________________________________________________________________________________________________


# Crea Frame-----------------------------------------------------------------------------------------
miFrame = Frame(raiz, width = 500, height = 400, bg = 'lightgray')
miFrame.pack()

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
botonIgual = Button(miFrame, padx = padX, pady = padY,text = '=', width = widthButtom,height = heigthButton).grid(row = 5, column = 3)
botonSum = Button(miFrame, padx = padX, pady = padY,text = '+', width = widthButtom, height = heigthButton).grid(row = 5, column = 4)



# Mantiene la ventana abierta
raiz.mainloop()

