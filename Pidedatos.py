#!/usr/bin/env python3
"""
@author: ISC juan luis Ordoñez perez
"""
import tkinter as tk #importamos la lo libreria que nos permitira hacer una grafica
ventana=tk.Tk()
ventana.title("APLICACION GRAFICA 1")
#anchoxalto en pixeles
ventana.geometry('500x700')
#color de fondo de la ventana
ventana.configure(background='dark turquoise')

#insertar imagen
image=tk.PhotoImage(file="1.gif")
image=image.subsample(4,4)
label=tk.Label(image=image)
label.pack()
#debe estar en .gif

e1=tk.Label(ventana,text="Ingresa Tu nombre: ",bg="black",fg="white")#imprimimos texto
e1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
entrada1=tk.Entry(ventana)#aqui es donde el texto se recibe
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(ventana,text="Ingresa Tu Apellido Paterno: ",bg="black",fg="white")#imprimimos texto
e2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
entrada2=tk.Entry(ventana)#aqui es donde el texto se recibe
entrada2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e3=tk.Label(ventana,text="Ingresa Tu Apellido Materno: ",bg="black",fg="white")#imprimimos texto
e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
entrada3=tk.Entry(ventana)#aqui es donde el texto se recibe
entrada3.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
"""
#insertar imagen de fondo
image=tk.PhotoImage(file="1.gif")
image=image.subsample(1,)
label=tk.Label(image=image)
label.place(x=0,y=0,relwidth=1.0,relheight=1.0)
#esto es para ponerlo de fondo de pantalla de la app
#debe estar en .gif
"""

ventana.mainloop()
