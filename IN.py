from tkinter import *
from tkinter import ttk
from tkinter import messagebox

raiz=Tk()
raiz.title(" Aplicacion de Torneo " )
#raiz.geometry("750x750")
raiz.config(bg="#A9A9E9")
raiz.columnconfigure(1, weight=1)
raiz.rowconfigure(1,weight=1)

FrameCampos=Frame(raiz)
FrameCampos.columnconfigure(0,weight=0)
FrameCampos.rowconfigure(0,weight=0)
FrameCampos.grid(row=0, column=0, sticky='nsew')
FrameCampos.config(bg="#E9F9E9")#color del frame
FrameCampos.config(width="1300", height="300")#Tamaño del fram, para que este surja efecto el de la raiz debe estar desactivado
FrameCampos.grid_propagate(0)
FrameCampos.config(bd=2)#tamaño al borde del frame
FrameCampos.config(relief="raised")#tipo de marco para el frame


Edadlabel=Label(FrameCampos,text="Edad ")
Edadlabel.grid(row=1,column=0,pady=4, padx=2)
txtEdad=Entry(FrameCampos)
txtEdad.grid(row=1,column=1,padx=8, pady=8)
txtEdad.focus()


def Resultado():
          Edad=txtEdad.get()
          if int(Edad) < 18:
                    print("El alumno es menor de edad ")
          else:
                    print("Alumno mayor de edad")
ingresarUsuarios=Button(FrameCampos,width=8, text="Insertar", command=Resultado)
ingresarUsuarios.config(bg="#008B8B", fg="#191970", font="cursiva")
ingresarUsuarios.grid(row=2, column=0)



#Alumno1.imprimir()
#Alumno1.Resultado(12)

raiz.mainloop()