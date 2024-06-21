import tkinter as tk

def on_button_click():
    print("¡Botón presionado!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de ventana con botón")

# Crear un botón en la ventana
boton = tk.Button(ventana, text="Presionar", command=on_button_click)
boton.pack(pady=20)  # pady es el padding vertical para separar elementos

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Crear un botón para cerrar la ventana
boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()