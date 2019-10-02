## GUI - Video 43

#-- Importación de librerías
from tkinter import *


# Crea la variable raíz (ventana principal)...................................................
raiz = Tk()
# Agrega título a la ventaba principal
raiz.title("Ventana de Pruebas")
    # Permite redimensionamiento horizontal y/o vertical
    # raiz.resizable(True, False)
    # Tamaño de la ventana raíz (la raíz se adapta al contenedor (frame))
    #raiz.geometry("650x350")
# Color de la ventana principal
raiz.config(bg="blue", cursor = "hand2")
#.............................................................................................
#--- Construcción del frame (ventana secundaria)----------------------------------------------
miFrame=Frame()
# Empacar el marco secundario - se puede configurar el posicionamiento dentro de la raíz
miFrame.pack(side = "left", anchor = "n")
    #miFrame.pack( fill = "both", expand = True)
# Condigurar 
miFrame.config(bg = 'red')
miFrame.config(width = '650', height = '350')

# Bordes-------------------------------------------------------------------------------------
miFrame.config(relief ="groove", bd = "35")

# Cursor-------------------------------------------------------------------------------------
miFrame.config(cursor = "hand2")
raiz.mainloop()





