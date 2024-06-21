import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading

# Configurar las opciones de Chrome
options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--disable-features=VizDisplayCompositor")
options.add_argument("--window-size=1920,1080")
# options.add_argument("--headless")  # Opcional: ejecutar en modo headless para depuración

# Configurar el servicio de Chrome y el controlador (ChromeDriver)
chrome_service = ChromeService(ChromeDriverManager().install())

# DataFrame para almacenar los datos del archivo Excel
df = pd.DataFrame()

# Función para cargar el archivo Excel y mostrar en la consola
def cargar_archivo():
    global df
    filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if filepath:
        df = pd.read_excel(filepath)
        print("Archivo cargado con éxito:")
        print(df.head())  # Mostrar los primeros registros en la consola
        messagebox.showinfo("Éxito", "Archivo Excel cargado correctamente.")

# Función para iniciar sesión en WhatsApp Web y enviar mensajes
def iniciar_sesion_whatsapp():
    driver = webdriver.Chrome(service=chrome_service, options=options)
    
    try:
        driver.get("https://web.whatsapp.com")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas'))
        )
        
        print("WhatsApp Web se ha cargado correctamente. Escanea el código QR.")
        
        # Mantener la sesión abierta
        input("Presiona Enter después de escanear el código QR para continuar...")
    
    except Exception as e:
        print(f"Error al cargar WhatsApp Web: {e}")
    
    finally:
        driver.quit()

# Función para enviar mensajes usando los datos del archivo Excel
def enviar_mensajes():
    global df
    if df.empty:
        messagebox.showwarning("Advertencia", "Por favor carga un archivo Excel primero.")
        return
    
    print("Enviando mensajes...")
    
    driver = webdriver.Chrome(service=chrome_service, options=options)
    
    try:
        driver.get("https://web.whatsapp.com")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas'))
        )
        
        # Esperar a que se cargue WhatsApp Web
        time.sleep(10)

        for index, row in df.iterrows():
            numero = str(row['+51590692976'])  # Convertir el número a cadena
            mensaje = row['GAAAAAAAAAAAA']

            # Abrir la conversación con el número
            driver.get(f"https://web.whatsapp.com/send?phone={numero}&text={mensaje}")
            time.sleep(5)

            # Enviar el mensaje
            send_button = driver.find_element(By.CSS_SELECTOR, 'span[data-icon="send"]')
            send_button.click()
            time.sleep(5)
        
        messagebox.showinfo("Envío Exitoso", "Mensajes enviados correctamente.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar mensajes en WhatsApp Web: {e}")
    
    

# Crear la ventana principal
root = tk.Tk()
root.title("Enviar Mensajes a WhatsApp desde Excel")

# Crear un botón para cargar el archivo Excel
boton_cargar = tk.Button(root, text="Subir Excel", command=cargar_archivo)
boton_cargar.pack(pady=20)

# Crear un botón para iniciar sesión en WhatsApp Web
boton_iniciar_sesion = tk.Button(root, text="Iniciar Sesión en WhatsApp", command=iniciar_sesion_whatsapp)
boton_iniciar_sesion.pack(pady=20)

# Crear un botón para enviar mensajes
boton_enviar = tk.Button(root, text="Enviar Mensaje", command=enviar_mensajes)
boton_enviar.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
