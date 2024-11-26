#!/usr/bin/env python3

# Creación del objeto tarea

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

#Función para mostar el menú de opciones
def mostrar_menu():
    print("\n[+] ¡Bienvenido al gestor de tareas!\n")
    print("Opciones:")
    print("1: Salir del programa")
    print("2: Crear una nueva tarea")
    print("3: Mostar tareas existentes")

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

    numero_de_tarea = str(len(tareas) + 1) #Calculamos el número de tarea
    tareas["tarea"+numero_de_tarea] = Tarea(titulo, contenido, status) #Creamos la nueva tarea
    print(f"\n[+] Se ha creado la tarea '{'tarea'+numero_de_tarea}':\n")
    print(tareas["tarea"+numero_de_tarea])

#Función para mostrar tareas existentes
def mostrar_tareas():

    print("\nA continuación se muestran las tareas existentes: \n")
    for tarea in tareas:

        print(f"{tarea}: '{tareas[tarea].titulo}'")


tareas = {} #Set donde se guardarán las tareas

# Bucle principal del programa
while True:
    
    mostrar_menu() #Mostramos el menú de opciones

    opcion = int(input("\n¿Qué es lo que desea hacer?\n")) #Solicitamos la instrucción de ejecución

    if opcion == 1:
        # Opción para cerrar el programa 
        print("\n[!] Saliendo del programa...\n")
        break
    elif opcion == 2:
        # Opción para crear la tarea
        crear_tarea()
    elif opcion == 3:
        #Opción para mostar tareas
        mostrar_tareas()
