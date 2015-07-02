import os

def creacion(nombre_archivo):
    archi=open(nombre_archivo,'w')
    archi.close()



def menu():
    print ""
    print "    Bienvenido a Creador de Archivos!"
    print ""
    print "    Ingresa el nombre del archivo que deseas crear"
    print ""
    nombre_archivo = raw_input("    Nombre: ")
    creacion(nombre_archivo)

menu()

