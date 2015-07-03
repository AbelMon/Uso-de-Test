#coding:utf-8
import os
import sys

def nombre_archivo():
    archivo = raw_input("    > Ingrese el nombre del archivo: ")
    return archivo

def creacion(archivo):
    archi=open(archivo,'w')
    archi.close()

def existe_archivo(archivo):
    return os.path.isfile(archivo)

def decidir_creacion(archivo):
    existe = existe_archivo(archivo)
    if existe == False:
        creacion(archivo)
        print ""
        print "    * Se ha creado el archivo ", archivo
        print ""
    else:
        print ""
        print "    Ya existe el archivo!"
        print ""

def eliminar_archivo(archivo):
    try:
        os.remove(archivo)
        print ""
        print "    * Se ha eliminado el archivo ", archivo
    except OSError:
        print ""
        print "    No existe el archivo"
        print ""

def funciones_creadoras():
    limpiar_pantalla()
    print ""
    print "    /* Creando archivos */"
    print ""
    
    archivo = nombre_archivo()
    solo_espacios = archivo.isspace()

    if len(archivo) > 0 and solo_espacios == False:
        decidir_creacion(archivo)
    else:
        print ""
        print "    Nombre de archivo inválido"
        print ""

    raw_input("    Regresando al menu. Presiona enter... ")


def funciones_eliminadoras():
    limpiar_pantalla()
    print ""
    print "    /* Eliminar archivos */"
    print ""
    archivo = nombre_archivo()
    eliminar_archivo(archivo)
    print ""
    raw_input("    Regresando al menu. Presiona enter... ")

def limpiar_pantalla():
    if os.name == "posix":
        os.system("reset")
    elif os.name == "nt":
        os.system("cls")

def menu():
    while True:
        limpiar_pantalla()
        print ""
        print "    Bienvenido a Gestor de Archivos!"
        print ""
        print "    Elige una opcion: "
        print ""
        print "    * Para crear un archivo ingresa '1'."
        print "    * Para eliminar un archivo ingresa '2'."
        print "    * Para salir ingresa '3'."
        print ""
        decision_usuario = raw_input("    > ")
        if decision_usuario == "1":
            funciones_creadoras()
        elif decision_usuario == "2":
            funciones_eliminadoras()
        elif decision_usuario == "3":
            sys.exit(0)
        else:
            print ""
            print "    Elige una opcion válida"
            print ""
            raw_input("    Presiona enter... ")



menu()

