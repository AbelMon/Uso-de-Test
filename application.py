import os

def creacion(nombre_archivo):
    archi=open(nombre_archivo,'w')
    archi.close()

def existe_archivo(archivo):
    return os.path.isfile(archivo)


def menu():
    print ""
    print "    Bienvenido a Creador de Archivos!"
    print ""
    print "    Ingresa el nombre del archivo que deseas crear"
    print ""
    nombre_archivo = raw_input("    Nombre: ")

menu()

