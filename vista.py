from tkinter import Tk, Frame, Label, StringVar, IntVar,Checkbutton, Button, ttk, Scrollbar

miVentana= Tk()
miVentana.title("Detector de colores")
miVentana.resizable(0,0)
miVentana.geometry("550x600")
estado_color = StringVar()
back_color = StringVar()
conx = StringVar()

conect = StringVar()
estaCorriendo = True
registrosT = StringVar()
modo = StringVar()
mode = 'n'




frame1 = Frame(miVentana)
frame1.pack(fill='both', expand=True)

frame2 = Frame(miVentana)
frame2.pack(fill='both', expand=True)

frame3 = Frame(miVentana)
frame3.pack(fill='both', expand=True)

frame4 = Frame(miVentana)
frame4.pack(fill='both', expand=True)

    

Label(frame1, text="..:: Detector de color ::..").grid(row=0,column=2, padx=5, pady=5, sticky="we")
Label(frame1, textvariable=estado_color, width=10, borderwidth=2, relief="groove", fg="white", bg="black", font=("Courier New", 15, "bold")).grid(row=2, column=2, padx=5, pady=5, sticky="we")
Label(frame1, text="..:: Estado ::..").grid(row=3,column=2, padx=5, pady=5, sticky="we")
Label(frame2, text="..:: Colores ::..").grid(row=5,column=2, padx=5, pady=5, sticky="we")

# Label(frame3, textvariable=registrosT, width=43, borderwidth=2, relief="groove", bg="white", fg="black", font=("Courier New", 15, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky="we")
Label(frame3, textvariable=conx).grid(row=3,column=0, padx=5, pady=5, sticky="we")


scroll = Scrollbar(frame3, orient="vertical")

tabla = ttk.Treeview(frame3,  columns=('1', '2', '3'), yscrollcommand=scroll.set)



tabla.grid(row=2,column=0, padx=5, pady=5, sticky="we")
scroll.grid(row=2, column=1, sticky='ns')
scroll.config(command=tabla.yview)

tabla.column("#0", width=130, anchor="center")
tabla.column("1", width=130, anchor="center")
tabla.column("2", width=130, anchor="center")
tabla.column("3", width=130, anchor="center")

tabla.heading("#0", text="Id")
tabla.heading("1", text="Color")
tabla.heading("2", text="Fecha")
tabla.heading("3", text="Hora")



boton1 = Button(frame1, width=10, text="Manual")
boton1.grid(row=4,column=1, padx=50, pady=3)

boton2 = Button(frame1, width=10, text="Automatico")
boton2.grid(row=4,column=3, padx=50, pady=3)

rojo = Button(frame2, width=10, text="Rojo")
rojo.grid(row=6,column=0, padx=10, pady=20)

blanco = Button(frame2, width=10, text="Blanco")
blanco.grid(row=6,column=1, padx=10, pady=20)

naranja = Button(frame2, width=10, text="Naranja")
naranja.grid(row=6,column=2, padx=10, pady=20)

verde = Button(frame2, width=10, text="Verde")
verde.grid(row=6,column=3, padx=10, pady=20)

azul = Button(frame2, width=10, text="Azul")
azul.grid(row=6,column=4, padx=10, pady=20)


def insertar_tabla(datos):
    registros = tabla.get_children()
    for registro in registros:
        tabla.delete(registro)
    for dato in datos:
        print(dato)
        tabla.insert("", 0, text=dato[0], values=(dato[1], dato[2], dato[3]))




# miVentana.mainloop()