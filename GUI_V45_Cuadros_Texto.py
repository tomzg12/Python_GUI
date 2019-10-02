## GUI   - Video 45

#-- Importación de librerías
from tkinter import *

# Crea la variable raíz (ventana principal)...................................................
root = Tk()

miFrame = Frame(root, width = 1200, height = 600)
miFrame.pack()

# Crea Labels
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

# Crea cajas de texto y las configura
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row = 0, 
                  column = 1, 
                  sticky = 'e',
                  padx = 10, pady = 10)
cuadroNombre.config(fg = 'red', justify = 'center')

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 1, 
                    column = 1, 
                    sticky = 'e', 
                    padx = 10, pady = 10)

cuadroPass = Entry(miFrame)
cuadroPass.grid( row = 2, 
                 column = 1, 
                 sticky = 'e', 
                 padx = 10, pady = 10)
cuadroPass.config(fg= 'blue', show ='*')

# Mantiene la ventana abierta
root.mainloop()

