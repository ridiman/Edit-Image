#!/usr/bin/python

import os
from PIL import Image
from PIL import ImageFilter
from time import sleep

logo="""
                                                                            \033[97m
    ██╗███╗░░░███╗░█████╗░░██████╗░███████╗███╗░░██╗███████╗░██████╗        \033[96m
    ██║████╗░████║██╔══██╗██╔════╝░██╔════╝████╗░██║██╔════╝██╔════╝        \033[94m
    ██║██╔████╔██║███████║██║░░██╗░█████╗░░██╔██╗██║█████╗░░╚█████╗░        \033[95m
    ██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░░╚═══██╗        \033[97m
    ██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗██║░╚███║███████╗██████╔╝        \033[90m
    ╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═════╝   v=1.0 \033[97m

"""
opciones=""" 
    1.Abrir Imagenes
    2.Editar Imagenes
    3.Cambiar Extencion
    4.Redimencionar Imagenes
    5.Salir 
"""
opciones2=""" 
    1.Contraste 
    2.Contraste suave
    3.Blanco / negro
    4.Retroceder
"""
opcion="""
    1.Guardar
    0.Retroceder
 """
opciones3="""
    1.Png
    2.Jpg
    3.Jpeg
    4.Retroceder
 """
def proceso(): # proceso de guardado
    for i in range(100):
        i+=1
        print (f"Guardando " , i , " %")
        os.system("clear")
    print("[*] Completo")

class Img:
    def __init__(self,name):
        self.name = name
    def Abrir_imagen(self):
        self.img=Image.open(self.name) # abrimos imagen
        self.img.show() # mostramos imagen
        input("")

    def Editar_imagen(self):
        os.system("clear") 
        print(opciones2)
        opc=int(input(">> ")) # opc = opcion para elegir
        if (opc==1):
            self.edit_img=Image.open(self.name)
            self.edit_img=self.edit_img.filter(ImageFilter.EDGE_ENHANCE_MORE) # despues de abrir lo ponemos filtro Nitides
            self.edit_img.show() # mostramos imagen
            os.system("clear")
            print(opcion) 
            opc2=int(input(">> ")) # opcion elegir 2
            if (opc2==1):
                self.edit_img.save(self.name) # guardamos imagen
                proceso() # imprimimos proceso
                input("")
            else:
                pass # retrocedemos de menu

        elif (opc==2):
            self.edit_img2=Image.open(self.name)
            self.edit_img2=self.edit_img2.filter(ImageFilter.SMOOTH_MORE) # filtro suave
            self.edit_img2.show()
            os.system("clear")
            print(opcion)
            opc3=int(input(">> ")) # opcion elegir 3
            if (opc3==1):
                self.edit_img2.save(self.name)
                proceso()
                input("")
            else:
                pass
            
        elif (opc==3):
            self.edit_img3=Image.open(self.name)
            self.edit_img3=self.edit_img3.convert("L") # filtro b/n
            self.edit_img3.show()
            os.system("clear")
            print(opcion)
            opc4=int(input(">> ")) # opcion elegir 4
            if (opc4==1):
                self.edit_img3.save(self.name)
                proceso()
                input("")
            else:
                pass 
        elif (opc==4):
            pass

    def Editar_extencion(self):
        self.cambiar_extencion=Image.open(self.name)
        os.system("clear")
        print(opciones3)
        e_e=int(input(">> ")) # elecion de extencion
        if (e_e==1):
            self.cambiar_extencion.save(self.name + ".png") # creamos nueva imagen con extencion png 
            proceso()
            input("")
        elif (e_e==2):
            self.cambiar_extencion.save(self.name + ".jpg") # extencion jpg
            proceso()
            input("")
        elif (e_e==3):
            self.cambiar_extencion.save(self.name + ".jpeg") # extencion jpeg
            proceso()
            input("")
        elif (e_e==4):
            pass

class Img_Resize:
    def __init__(self,name,alto,ancho): 
        self.name=name
        self.alto=alto
        self.ancho=ancho

    def Redimencionar(self):
        os.system("clear")
        self.img=Image.open(self.name)
        self.new_img=self.img.resize((self.alto,self.ancho)) 
        self.new_img.show()
        print(opcion)
        e_r=int(input(">> ")) # eleccion de resizablecion
        if (e_r==1):
            self.new_img.save(self.name)
            proceso()
            input("")
        elif (e_r==2):
            pass

while True:
    os.system("clear") # limpiamos pantalla
    print (logo)
    print (opciones)
    e_o=int(input(">> ")) # elecion de opciones
    if (e_o==1):
        nombre_imagen=input("\n Nombre Imagen : ") 
        a=Img(nombre_imagen) 
        print(a.Abrir_imagen()) 
        pass

    elif (e_o==2):
        nombre_imagen=input("\n Nombre Imagen : ")
        a=Img(nombre_imagen)
        print(a.Editar_imagen())

    elif (e_o==3):
        nombre_imagen=input("\n Nombre Imagen : ")
        a=Img(nombre_imagen)
        print(a.Editar_extencion())

    elif (e_o==4):
        nombre_imagen=input("\n Nombre Imagen : ")
        alto_imagen=int(input(" Alto de la imagen : "))
        ancho_imagen=int(input(" Ancho de la imagen : "))
        a=Img_Resize(nombre_imagen,alto_imagen,ancho_imagen)
        print(a.Redimencionar())

    elif (e_o==5):
        exit() # salir

        
