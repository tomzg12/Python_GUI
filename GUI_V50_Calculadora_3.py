## GUI  - Video 50
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
reset_pantalla=False

#____________________________________________________________________________________________________
# FUNCIONES
 # Pulsación de teclado
def numeroPulsado(num):
    
	global operacion

	global reset_pantalla

	if reset_pantalla!=False:

		numeroPantalla.set(num)

		reset_pantalla=False

	else:
	
		numeroPantalla.set(numeroPantalla.get() + num)
    
# Operación de suma
def suma(num):
    
	global operacion

	global resultado

	global reset_pantalla

	resultado+=int(num) #resultado=resultado+int(num)

	operacion="suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)

# Resta
#---------------funcion resta------------------------------
num1=0

contador_resta=0


def resta(num):
    
	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True

#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=int(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------



contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True



#----------------funcion el_resultado----------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+int(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

		resultado=0

		contador_divi=0

	



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
botonDiv = Button(miFrame, padx = padX, pady = padY,text = '/', width = widthButtom, height = heigthButton,command=lambda:divide(numeroPantalla.get())).grid(row = 2, column = 4)
#Fila 2
boton4 = Button(miFrame, padx = padX, pady = padY,text = '4', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('4')).grid(row = 3, column = 1)
boton5 = Button(miFrame,padx = padX, pady = padY, text = '5', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('5')).grid(row = 3, column = 2)
boton6 = Button(miFrame, padx = padX, pady = padY,text = '6', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('6')).grid(row = 3, column = 3)
botonMult = Button(miFrame, padx = padX, pady = padY,text = 'X', width = widthButtom, height = heigthButton, command=lambda:multiplica(numeroPantalla.get())).grid(row = 3, column = 4)
#Fila 3
boton1 = Button(miFrame, padx = padX, pady = padY,text = '1', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('1')).grid(row = 4, column = 1)
boton2 = Button(miFrame, padx = padX, pady = padY,text = '2', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('2')).grid(row = 4, column = 2)
boton3 = Button(miFrame, padx = padX, pady = padY,text = '3', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('3')).grid(row = 4, column = 3)
botonRest = Button(miFrame, padx = padX, pady = padY,text = '-', width = widthButtom,height = heigthButton, command=lambda:resta(numeroPantalla.get())).grid(row = 4, column = 4)
#Fila 4
boton0 = Button(miFrame, padx = padX, pady = padY,text = '0', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('0')).grid(row = 5, column = 1)
botonComa = Button(miFrame, padx = padX, pady = padY,text = '.', width = widthButtom, height = heigthButton,command = lambda:numeroPulsado('.')).grid(row = 5, column = 2)
botonIgual = Button(miFrame, padx = padX, pady = padY,text = '=', width = widthButtom,height = heigthButton, command = lambda: el_resultado()).grid(row = 5, column = 3)
botonSum = Button(miFrame, padx = padX, pady = padY,text = '+', width = widthButtom, height = heigthButton, command = lambda:suma(numeroPantalla.get())).grid(row = 5, column = 4)



# Mantiene la ventana abierta
raiz.mainloop()

