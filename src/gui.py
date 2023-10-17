import tkinter as tk


def on_button_click():
    if label["text"] == "Presiona el botón:":
        label["text"] = "¡Hola, mundo!"
    else:
        label["text"] = "Presiona el botón:"


app = tk.Tk()
app.geometry("700x700")
app.title("Ejemplo con Tkinter")

label = tk.Label(app, text="Presiona el botón:")
label.pack(padx=20, pady=20)

button = tk.Button(app, text="Haz clic", command=on_button_click)
button.pack()

app.mainloop()
