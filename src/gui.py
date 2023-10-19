import tkinter
from tkinter import *

num_days = 0
num_clients = 0
matriz = []


app = tkinter.Tk()
app.title("Plantas de Energı́a")
app.geometry("900x900")

etiqueta = tkinter.Label(app, text="Plantas de Energı́a", font=(
    'Times New Roman', 15), pady=5, padx=0)
etiqueta.place(x=150, y=20)

lb_clients = Label(app, text="Ingrese el número de clientes =>")
lb_clients.place(x=20, y=80)

lb_days = Label(app, text="Ingrese el número de días =>")
lb_days.place(x=20, y=120)

input_clients = Entry(app, width=10)
input_clients.place(x=230, y=80)

input_days = Entry(app, width=10)
input_days.place(x=230, y=120)

matriz


def init_Tb_paymenst(num_clients: int):
    columnas = []
    for i in range(2):
        filas = []
        for j in range(num_clients):
            e = Entry(app, relief=RIDGE)
            if i == 0:
                e.insert(END, f'Cliente {j+1}')
            e.place(x=40+i*160, y=215+j*20)
            filas.append(e)
        columnas.append(filas)

    matriz.append(columnas)


def clickStart():
    global num_clients

    try:
        num_clients = int(input_clients.get(), 10)
        init_Tb_paymenst(num_clients)
    except:
        IndexError


boton_cargar = Button(
    app, text="Iniciar carga de datos", command=clickStart, width=25)
boton_cargar.place(x=350, y=80)

label_topic = Label(app, text="Clientes", font=('Times New Roman', 12))
label_topic.place(x=65, y=190)
label_min = Label(app, text="Pago", font=('Times New Roman', 12))
label_min.place(x=220, y=190)

app.mainloop()
