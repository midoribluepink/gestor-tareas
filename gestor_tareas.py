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


