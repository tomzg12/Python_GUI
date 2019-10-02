## GUI   - Video 44

#-- Importación de librerías
from tkinter import *

# Crea la variable raíz (ventana principal)...................................................
root = Tk()

miFrame = Frame(root, width ="800", height = "600")

miFrame.pack()
# Etiquetas de texto...................................................
                    #Label(miFrame, text = "Mensaje de prueba", 
                        # fg = "red", font= ("Arial", 18)).place(x = "100", y = "200") 

# Imágen ..............................................................
miImagen = PhotoImage(file = "Avocado.png")
Label(miFrame, image = miImagen).place(x = "100", y = "100") 

root.mainloop()


