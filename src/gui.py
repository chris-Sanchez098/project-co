import tkinter as tk
from tkinter import Entry
from tkinter import Scrollbar
from tkinter.font import Font
from tkinter import Label
from tkinter import Button
from tkinter import END
from tkinter import RIDGE
from utils import *


num_days = 0
num_clients = 0
matriz = []

# Methods


def set_container_color(container, color):
    container.configure(bg=color)


def init_tb_payments(num_clients: int):
    columnas = []
    for i in range(2):
        filas = []
        for j in range(num_clients):
            text = f'Cliente {j+1}' if i == 0 else ""
            e = Entry(container4, text=text)
            e_window = container4.create_window(
                (4+i*160, 20+j*20), window=e, anchor="nw")
            filas.append(e)
        columnas.append(filas)
    matriz.append(columnas)


def clickStart():
    global num_clients
    try:
        lb_clients_c4 = tk.Label(
            container4, text="Clientes", font=('Times New Roman', 12))
        lb_pago_c4 = tk.Label(container4, text="Pago",
                              font=('Times New Roman', 12))

        lb_clients_c4_window = container4.create_window(
            (50, 0), window=lb_clients_c4, anchor="nw")

        lb_pago_c4_window = container4.create_window(
            (200, 0), window=lb_pago_c4, anchor="nw")
        num_clients = int(input_clients.get(), 10)
        # Agregar entradas a container4
        init_tb_payments(num_clients)
    except IndexError:
        pass  # Manejo de excepción


def on_horizontal_scroll(event):
    container = event.widget
    if event.delta > 0:
        container.xview_scroll(-1, "units")
    else:
        container.xview_scroll(1, "units")


root = tk.Tk()
root.title("Plantas de Energı́a")

# Setup rows and columns for distribution
root.grid_rowconfigure(0, weight=5)
root.grid_rowconfigure(1, weight=15)
root.grid_rowconfigure(2, weight=35)
root.grid_rowconfigure(3, weight=45)  # container6
root.grid_columnconfigure(0, weight=50)
root.grid_columnconfigure(1, weight=50)

# Create containers
container1 = tk.Frame(root)
container2 = tk.Frame(root)
container3 = tk.Frame(root)

container4 = tk.Canvas(root)
scrollbar4_y = Scrollbar(container4, orient="vertical")
scrollbar4_x = Scrollbar(container4, orient="horizontal")
container4.config(yscrollcommand=scrollbar4_y.set,
                  xscrollcommand=scrollbar4_x.set)
scrollbar4_y.config(command=container4.yview)
scrollbar4_x.config(command=container4.xview)
container4.bind("<MouseWheel>", on_horizontal_scroll)

container5 = tk.Canvas(root)
scrollbar5_y = Scrollbar(container5, orient="vertical")
scrollbar5_x = Scrollbar(container5, orient="horizontal")
container5.config(yscrollcommand=scrollbar5_y.set,
                  xscrollcommand=scrollbar5_x.set)
scrollbar5_y.config(command=container5.yview)
scrollbar5_x.config(command=container5.xview)

container6 = tk.Canvas(root)
scrollbar6_y = Scrollbar(container6, orient="vertical")
scrollbar6_x = Scrollbar(container6, orient="horizontal")
container6.config(yscrollcommand=scrollbar6_y.set,
                  xscrollcommand=scrollbar6_x.set)
scrollbar6_y.config(command=container6.yview)
scrollbar6_x.config(command=container6.xview)

container1.grid(row=0, column=0, columnspan=2, sticky="nsew")
container2.grid(row=1, column=0, sticky="nsew")
container3.grid(row=1, column=1, sticky="nsew")

container4.grid(row=2, column=0, sticky="nsew")
scrollbar4_y.pack(side="right", fill="y")
scrollbar4_x.pack(side="bottom", fill="x")

container5.grid(row=2, column=1, sticky="nsew")
scrollbar5_y.pack(side="right", fill="y")
scrollbar5_x.pack(side="bottom", fill="x")

container6.grid(row=3, column=0, columnspan=2, sticky="nsew")
scrollbar6_y.pack(side="right", fill="y")
scrollbar6_x.pack(side="bottom", fill="x")

# Set containers colors / temp
set_container_color(container5, "green")
set_container_color(container6, "lightcoral")

# Containers data

# container1
title_font = Font(family="Arial", size=20, weight="bold")
title_label = tk.Label(container1, text="Plantas de Energía", font=title_font)
title_label.pack(fill="both", expand=True)

# container2
lb_clients = Label(container2, text="Ingrese el número de clientes =>")
lb_clients.place(x=20, y=10)

lb_days = Label(container2, text="Ingrese el número de días =>")
lb_days.place(x=20, y=30)

input_clients = Entry(container2, width=10)
input_clients.place(x=230, y=10)
input_clients.configure(validate="key", validatecommand=(
    input_clients.register(validate_int_input), "%P"))

input_days = Entry(container2, width=10)
input_days.place(x=230, y=30)
input_days.configure(validate="key", validatecommand=(
    input_days.register(validate_int_input), "%P"))

boton_cargar = Button(
    container2, text="Iniciar carga de datos", command=clickStart, width=25)
boton_cargar.place(x=50, y=60)

# container3
content3 = tk.Label(container3, text="Contenedor 3")
content3.pack()


# Add content to containers 4, 5 and 6 using canvas
content5 = tk.Label(container5, text="Contenedor 5")
content5_window = container5.create_window(
    (0, 0), window=content5, anchor="nw")
content6 = tk.Label(container6, text="Contenedor 6")
content6_window = container6.create_window(
    (0, 0), window=content6, anchor="nw")

# Set scrollregion to update scrollbars
container4.update_idletasks()
container5.update_idletasks()
container6.update_idletasks()

container4.config(scrollregion=container4.bbox("all"))
container5.config(scrollregion=container5.bbox("all"))
container6.config(scrollregion=container6.bbox("all"))

# Start the application
root.geometry("800x600")
root.mainloop()
