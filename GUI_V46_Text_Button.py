## GUI  - Video 46

#-- Importación de librerías
from tkinter import *

# Crea la variable raíz (ventana principal)----------------------------------------------------------
root = Tk()

# Crea Frame------------------------------------------------------------------------------------------
miFrame = Frame(root, width = 1200, height = 600)
miFrame.pack()

#---Sección de variables------------------------------------------------------------------------------
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()

#  FUNCIONES__________________________________________________________________________________________

def codigoBoton():
    miNombre.set('Tom')
    miApellido.set('ZG')
    miPass.set('password')
    
    
# Crea Labels-----------------------------------------------------------------------------------------
nombreLabel = Label(miFrame, text = 'Nombre :')
nombreLabel.grid(row = 0, column = 0, 
                 sticky = 'e', 
                  padx = 10, pady = 10)
apellidoLabel = Label(miFrame, text = 'Apellido :')

apellidoLabel.grid(row = 1, column = 0, 
                 sticky = 'e', 
                 padx = 10, pady = 10)

passLabel = Label(miFrame, text = 'Password :')
passLabel.grid(row = 2, column = 0, 
                 sticky = 'e', 
                 padx = 10, pady = 10)

commentLabel = Label(miFrame, text = 'Comentarios :')
commentLabel.grid(row = 3, column = 0, 
                 sticky = 'e', 
                 padx = 10, pady = 10)


# Crea cajas de texto y las configura----------------------------------------------------------------

cuadroNombre = Entry(miFrame, textvariable = miNombre)  # 1
cuadroNombre.grid(row = 0, 
                  column = 1, 
                  sticky = 'e',
                  padx = 10, pady = 10)
cuadroNombre.config(fg = 'red', justify = 'center')

cuadroApellido = Entry(miFrame, textvariable = miApellido)  # 2
cuadroApellido.grid(row = 1, 
                    column = 1, 
                    sticky = 'e', 
                    padx = 10, pady = 10)

cuadroPass = Entry(miFrame, textvariable = miPass)  #3
cuadroPass.grid( row = 2, 
                 column = 1, 
                 sticky = 'e', 
                 padx = 10, pady = 10)
cuadroPass.config(fg= 'blue', show ='*')

#--Cuadro de Texto
cuadroComment = Text(miFrame, width = 15, height = 15)  #4
cuadroComment.grid( row = 3, 
                    column = 1, 
                    sticky = 'e', 
                    padx = 10, pady = 10)

# Scroll (configuración)
scrollVert = Scrollbar(miFrame, 
                       command = cuadroComment.yview,  # yview = vertical
                       )
scrollVert.grid(row = 3, column = 2, 
                sticky = 'nsew'    # Se adapta al tamaño del Widget
                )

cuadroComment.config(  fg= 'gray'
                     , yscrollcommand = scrollVert.set  # scroll indica posición del texto
                     , bg = 'lightgray')


# Construcción de botones-----------------------------------------------------------------------------------
botonEnvio = Button( root
                    , text = 'Enviar'
                    , command = codigoBoton       # Desencadenar acción con botones
                    )
botonEnvio.pack()

# Mantiene la ventana abierta
root.mainloop()

