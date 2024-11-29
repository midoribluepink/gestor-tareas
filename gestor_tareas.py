#!/usr/bin/env python3

import json, os

# Creación del objeto tarea

tareas = {} #Dict donde se guardarán las tareas

class Tarea():

    def __init__(self, titulo, contenido = "", status = False): #Constructor de la clase

        self.titulo = titulo
        self.contenido = contenido
        self.status = status

    def __str__(self): #Método que permite imprimir las características de la tarea

        if self.contenido != "":
            return f"Tarea: {self.titulo}\n Descripción: {self.contenido}\n Status: {'Completada' if self.status else 'No completada'}\n"
        else:
            return f"Tarea: {self.titulo}\n Status: {'Completada' if self.status else 'No completada'}\n"

    def cambiar_status(self, status): # Método para cambiar el estatus de la tarea

        self.status = status
        return f"El estatus de {self.titulo} es {'Completada' if self.status else 'No completada'}"

    def agregar_notas(self, nota): # Método que permite agregar notas a las tareas existentes

        self.contenido += f"\n Nota: {nota}"

    def modificar_contenido(self, contenido): # Método que permite cambiar completamente la descripción de una tarea

        self.contenido = contenido

    def to_dict(self): #Método que convierte una instancia en un diccionario

        return {
            "titulo": self.titulo,
            "contenido": self.contenido,
            "status": self.status,
        }

    @staticmethod
    def from_dict(datos): #Método para crear una instancia desde un diccionario

        return Tarea(datos["titulo"], datos["contenido"], datos["status"])

# Función para guardar tareas en archivo
def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        #Las tareas pasan a ser una lista de diccionarios
        json.dump({k: v.to_dict() for k, v in tareas.items()}, archivo, indent = 4)

    print("[+] Las tareas han sido guardadas en 'tareas.json'")

def cargar_tareas():
    global tareas
    try:
        with open("tareas.json", "r") as archivo: #Abre el archivo con tareas
            datos = json.load(archivo)
            tareas = {k: Tarea.from_dict(v) for k, v in datos.items()}

        print("[+] Las tares han sido cargadas desde 'tareas.json'")
    except FileNotFoundError:
        #Si no se encuentra el archio se archivo se crea uno nuevo
        print("[!] No se encontró el archivo 'tareas.json'. Se iniciará una lista vacía")
        tareas = {}
    except excepcion as e:
        print(f"[!] Ocurrió un error al cargar las tareas: {e}. Se iniciará una lista vacía")
        tareas = {}

#Función para mostar el menú de opciones
def mostrar_menu():
    print("\n[+] ¡Bienvenido al gestor de tareas!\n")
    print("Opciones:")
    print("1: Salir del programa")
    print("2: Crear una nueva tarea")
    print("3: Mostrar tareas existentes")
    print("4: Mostrar detalles de una tarea existente")
    print("5: Modificar tareas")
    print("6: Eliminar tarea")

#Función par añadir una nueva tarea a la lista
def crear_tarea():
    print("\n[+] ¡Vamos a crear una nueva tarea!\n")
    titulo = input("Inserte el título de la nueva tarea: \n") #Solicitamos el título de la tarea
    contenido = input("Inserte el contenido de la tarea: \n") #Solicitamos el contenido de la tarea
    status = None

    while True:

        user_input = input("Inserte el status de la tarea (True/False)\n") #Pedimos el status de la tarea
        if user_input.lower() == "true":
            status = True
            break
        elif user_input.lower() == "false":
            status = False
            break
        else:
            print("\n[!] Por favor inserte un valor válido\n")

    numero_de_tarea = len(tareas) + 1 #Calculamos el número de tarea
    while True:
        # Bucle que nos permite no repetir números de tarea y se le asignará el número siguente más próximo disponible

        if "tarea"+str(numero_de_tarea) in tareas.keys():

            numero_de_tarea+=1 
        else:

            tareas["tarea"+str(numero_de_tarea)] = Tarea(titulo, contenido, status) #Creamos la nueva tarea
            break

    print(f"\n[+] Se ha creado la tarea '{'tarea'+str(numero_de_tarea)}':\n")
    print(tareas["tarea"+str(numero_de_tarea)])

#Función para mostrar tareas existentes
def mostrar_tareas():

    if len(tareas) == 0: # Comprobamos si hay tareas existentes
        print("\n[!] No hay tareas por el momento\n")

    print("\n[+] A continuación se muestran las tareas existentes: \n")
    for tarea in tareas: #Listamos las tareas existente

        print(f"{tarea}: '{tareas[tarea].titulo}'")

# Función par mostrar detalles
def mostrar_detalles():
    print("\n[+] Vamos a ver las tareas en detale\n")
    tarea = input("¿Qué tarea desea ver con detalle? \n")
    if tarea in tareas:
        print(f"A continuación se muestran los detalles de '{tarea}':\n")
        print(tareas[tarea])
    else:
        print("\n[!] Por favor proporcione una tarea existente\n")

# Función para modificar tareas
def modifcar_tarea():
    print("\n[+] Vamos a modificar las tareas\n")
    tarea = input("¿Qué tarea quiere modificar?\n") #Solicitamos la tarea a modificar
    if tarea in tareas: #Comprobamos que exista

        while True: #Bucle que permite equivocarse en la selección de modificación
            try: #Manejo de excepción que asegura que se coloque un número
                opcion = int(input("¿Qué desea modificar? (1: Contenido. 2: Status. 3: Agregar notas.):\n")) #Guardamos la opción
                if opcion == 1:
                    #Cambiar el contenido de la tarea
                    print("\n[+] Vamos a modificar el contenido de la nota\n")
                    contenido = input("Inserte la nueva descripción: ") #Pedimos la nueva descripción
                    print(f"\n[+] Se reemplazó '{tareas[tarea].contenido}' por '{contenido}'\n")
                    tareas[tarea].contenido = contenido #Cambiamos la descripción de la tarea
                    break
                elif opcion == 2:
                    #Modificar el status de la tarea
                    print("\n[+] Vamos a modificar el status de la nota\n")

                    while True: #Bucle que permite equivocarse en el input de status de tarea

                        status = None
                        user_input = input("Inserte el nuevo status de la tarea (True/False)\n") #Pedimos el status de la tarea
                        if user_input.lower() == "true":
                            status = True
                            break
                        elif user_input.lower() == "false":
                            status = False
                            break
                        else:
                            print("\n[!] Por favor inserte un valor válido\n")

                    print(f"\n[+] Se cambió el status de '{'Completada' if tareas[tarea].status else 'No completada'}' a '{'Completada' if status else 'No completada'}'")
                    tareas[tarea].status = status #Modificamos el status de la tarea
                    break
                elif opcion == 3:
                    #Agregar una nota a la descripción de la tarea
                    print("\n[+] Vamos a agregar una nota a la tarea\n")
                    nota = input("Inserte la nota que desea agregar: ")
                    tareas[tarea].agregar_notas(nota)
                    print(f"\n[+] Se agregó la nota a la descripción de la tarea:\n\nDescripción:\n\n'{tareas[tarea].contenido}'")
                    break
                else:
                    print("\n[!] Por favor proporcione un número válido\n")

            except:
                print("\n[+] Por favor proporcione un número\n")
         
    else:

        print("\n[!] Por favor proporcione una tarea válida\n")

# Función para eliminar taras
def eliminar_tarea():
    print("\n[+] Vamos a eliminar tareas \n")
    tarea = input("¿Qué tarea desea eliminar?:\n")
    # Bucle para validar la opción (y/n)
    while True:
        if tarea in tareas: #Comprobamos si la tarea existe
            opcion = input(f"¿Seguro que desea eliminar '{tareas[tarea].titulo}'? (y/n)\n")
            if opcion.lower() == "y": #Validad qué opción elige el usuario
                del tareas[tarea]
                print("\n[+] Se ha eliminado la tarea\n")
                break
            elif opcion.lower() == "n":
                print("\n[+] No se eliminó la tarea\n")
                break
            else:
                print("\n[+] Por favor inserte una opción válida\n")
        else:
            print("\n[!] La tarea no existe\n")
            break

cargar_tareas()
# Bucle principal del programa
while True:

    mostrar_menu() #Mostramos el menú de opciones

    try:
        opcion = int(input("\n¿Qué es lo que desea hacer?\n")) #Solicitamos la instrucción de ejecución
    except ValueError:
        print("\n[!] Por favor proporcione un número como opción\n")
        continue

    if opcion == 1:
        # Opción para cerrar el programa 
        print("\n[!] Saliendo del programa...\n")
        break
    elif opcion == 2:
        # Opción para crear la tarea
        os.system("clear")
        crear_tarea()
    elif opcion == 3:
        #Opción para mostar tareas
        os.system("clear")
        mostrar_tareas()
    elif opcion == 4:
        #Opción para mostrar detalles
        os.system("clear")
        mostrar_detalles()
    elif opcion == 5:
        #Opción par modificar tareas
        os.system("clear")
        modifcar_tarea()
    elif opcion == 6:
        #Opción para eliminar tareas
        os.system("clear")
        eliminar_tarea()
    else:
        print("\n[!] Por favor proporcione una opción válida\n")


guardar_tareas() #Guardar tareas
