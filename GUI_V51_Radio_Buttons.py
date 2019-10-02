## GUI - Video 51

#-- Importación de librerías
from tkinter import *
# Crea la variable raíz (ventana principal)...................................................
root = Tk()

# Variables
varOpcion = IntVar()


# Funciones
def imprimir():
    #print(varOpcion.get())
    if varOpcion.get() == 1:
        etiqueta.config(text = "Has elegido masculino")
    elif varOpcion.get() == 2:
        etiqueta.config(text = "Has elegido femenino")    
    else:
        etiqueta.config(text = "Has elegido otro")

# Etiquetas
Label(root, text= "Genero:").pack()

# Crea radio buttons
Radiobutton(root, text = 'Masculino', 
            variable = varOpcion, value = 1, 
            command = imprimir).pack()


Radiobutton(root, text = 'Femenino', 
            variable= varOpcion, value = 2,
            command = imprimir).pack()

Radiobutton(root, text = 'Otro', 
            variable= varOpcion, value = 3,
            command = imprimir).pack()

# Imprime etiqueta dentro de la raíz
etiqueta = Label(root)
etiqueta.pack()



# Venta abierta
root.mainloop()





