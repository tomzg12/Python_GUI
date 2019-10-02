## GUI - Video 51

#-- Importación de librerías
from tkinter import *
# Crea la variable raíz (ventana principal)...................................................
root = Tk()
root.title("Check button")


# Variables
foto  = PhotoImage(file = 'Avocado.png')
Label(root, image = foto).pack() 

playa = IntVar()
montagna = IntVar()
turRural = IntVar()



# Funciones
def opcionesViaje():
    opcionEscogida = ""
    if(playa.get() == 1):
        opcionEscogida += " Playa"
    
    if(montagna.get() == 1):
        opcionEscogida += " Montaña"

    if(turRural.get() == 1):
        opcionEscogida += " Turismo Rural"

    textoFinal.config(text= opcionEscogida)

# Etiqueta
frame = Frame(root)
frame.pack()
Label(frame, text = 'Elige destinos', width = 50).pack()

# Construye botones
Checkbutton(frame, text = 'Playa', 
            variable = playa, onvalue = 1,
                              offvalue = 0,
                              command = opcionesViaje).pack()


Checkbutton(frame, text = 'Montaña', 
            variable = montagna, onvalue = 1,
                              offvalue = 0,
                              command = opcionesViaje).pack()


Checkbutton(frame, text = 'Turismo rural', 
            variable = turRural, onvalue = 1,
                              offvalue = 0,
                              command = opcionesViaje).pack()



# Muestra etiqueta que muestra la variable elegida


textoFinal = Label(frame)
textoFinal.pack()


# Venta abierta
root.mainloop()





