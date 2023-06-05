import  tkinter as tk

def imprimir_saludo():
    label.config(text=f"Hola, {valor_nombre.get()}")


root = tk.Tk()
root.title("Calculadora tkinter")

root.geometry("800x600+400+200")

label = tk.Label( root, text="", bd=2, relief=tk.RAISED, width=50)
label.pack()

valor_nombre = tk.StringVar()


nombre = tk.Entry(root, textvariable=valor_nombre)
nombre.pack()

boton = tk.Button(root, text="pulsame", command=imprimir_saludo)
boton.pack()

root.mainloop()
