import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pyautogui
import webbrowser
from time import sleep

def upload_file():
    try:
        # Abrir un diálogo para seleccionar el archivo
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            # Leer el archivo Excel omitiendo la primera fila
            df = pd.read_excel(file_path, skiprows=1, header=None)
            
            # Asignar nombres a las columnas
            df.columns = ['numero', 'mensaje']
            
            # Convertir a listas
            numeros = df['numero'].tolist()
            mensajes = df['mensaje'].tolist()

            # Enviar mensajes
            send_messages(numeros, mensajes)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def send_messages(numeros, mensajes):
    # Abrir WhatsApp Web
    webbrowser.open('https://web.whatsapp.com')
    sleep(20)  # Espera a que se abra WhatsApp Web

    for numero, mensaje in zip(numeros, mensajes):
        try:
            # Abrir el chat del contacto directamente en una nueva pestaña
            url = f'https://web.whatsapp.com/send?phone=+51{numero}'
            webbrowser.open_new_tab(url)
            sleep(10)  # Espera a que se abra el chat del contacto

            # Escribir y enviar el mensaje
            pyautogui.typewrite(mensaje)
            pyautogui.press('enter')
            sleep(2)  # Espera a que se envíe el mensaje antes de pasar al siguiente

            # Cerrar la pestaña actual de WhatsApp Web
            pyautogui.hotkey('ctrl', 'w')
            sleep(2)  # Espera breve antes de abrir la siguiente pestaña

        except Exception as e:
            messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Subir archivo Excel")

# Crear un botón para subir el archivo
upload_button = tk.Button(root, text="Subir archivo Excel", command=upload_file)
upload_button.pack(pady=80)
upload_button.pack(padx=80)

# Ejecutar el bucle principal de la ventana
root.mainloop()
