## Gestor de tareas escrito en Python
Realizado por: **midoribluepink** a modo de práctica

Es un gestor de tareas simple para terminales Linux que nos permite crear tareas sencillas con un título, una descripción y un status (Completado/ No completado). Creado con la finalidad de tener un control de las actividades a realizar.

### Funcionamiento

El programa al ejecutarse buscará el archivo *tareas.json*, si no lo encuentra creará uno desde cero. En él, se guardarán las taeas que vayamos creando.

Para ejecutar el programa basta con hacer:

```shell
python3 gestor_tareas.py
```
y aparecerá el siguiente menú:

![image](https://github.com/user-attachments/assets/5da501f8-8ab1-4f9d-a050-d4d87310f390)

donde nos indica que no se ha encontrado el archivo de tareas y creará uno nuevo. Esto solo ocurrirá la primera vez. Después despliega el menú de opciones.

### 1. Salir del programa

Para salir del programa solo es necesario proporcionar el número 1.

### 2. Crear una nueva tarea

Al proporcionar el número 2 el programa entrará en fase de creación de nueva tarea:

![image](https://github.com/user-attachments/assets/35d46502-b10c-466d-8537-022aa8b6d2e5)

donde nos pedirá el título, el contenido o descripción y el status de la tarea. Al crearse se le asignará el nombre *tarea* más el número de tarea que le corresponda.

![image](https://github.com/user-attachments/assets/d12f6799-f526-472c-b6da-e247294cf38a)

### 3. Mostrar tareas existentes

Al proporcionar la tercera opción con el número 3 se generará una lista de las tareas existentes y se mostrará como única información el título de las mismas, esto con el fin de no saturar la pantalla en dado caso de que haya muchas tareas.

![image](https://github.com/user-attachments/assets/a93581a5-62bc-4497-bf33-097a88fa693a)

### 4. Mostrar detalles de una tarea existente

Como la opción anterior solo muestra el título de las tareas que lista, esta opción está pensada para ver toda la información de una tarea específica. Al seleccionarla proporcionando el número 4 veremos lo siguiente:

![image](https://github.com/user-attachments/assets/445cdd5d-8690-45bc-a17d-58037c757911)

y al seleccionar una tarea, mostrará toda la información de la misma:

![image](https://github.com/user-attachments/assets/430e6a04-b51e-4be9-95cd-e66ef5a40fac)

### 5. Modificar tareas

Al proporcionar el parámetro 5 podremos acceder al menú de modificación de tarea. Donde primero nos solicitará la tarea a modificar y, de existir la tarea, podremos cambiar sus propiedades:

![image](https://github.com/user-attachments/assets/ea24c587-250c-4a90-ab03-2a2b2cc3060e)

#### 1. Contenido

Al seleccionar esta opción podremos reemplazar toda la descripción de la nota. Es decir, se borrará la descripción y se agregará una nueva desde cero:

![image](https://github.com/user-attachments/assets/6c2b907d-8a8c-4efe-bdc3-82d3477495d8)

#### 2. Status

Con esta opción podremos marcar que hemos completado o no una tarea:

![image](https://github.com/user-attachments/assets/78d99ea6-9ff5-4b16-9617-54f543d51276)

#### 3. Agregar notas

La opción 3, agregar notas, sirve por si queremos añadir información adicional a una tarea sin necesidad de borrar la descripción inicial que dimos. Esta nueva información aparecerá con el prefijo *nota:*

![image](https://github.com/user-attachments/assets/7a9c6b84-ab43-4cbb-aee6-e806b508624e)

### 6. Eliminar tarea

La última opción es para deshacernos de tareas que ya no nos son útiles. Para acceder a esta característica es necesario proporcionar el parámetro 6, el nombre de la tarea y una confirmación para eliminarla.

![image](https://github.com/user-attachments/assets/cb9d19e1-3eac-48c5-b74c-8bfcee44a1f5)

