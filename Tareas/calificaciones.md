# Tarea: Registro de Calificaciones con Diccionarios Anidados

## Tema
Diccionarios dentro de diccionarios + Menús interactivos en Python.

## Objetivo
Practicar cómo almacenar información estructurada (alumnos → materias → calificaciones) en Python usando **diccionarios anidados**, y reforzar el uso de **bucles**, **condicionales** y **entradas por teclado** (`input()`).

---

## 📋 Instrucciones

1. Crea un diccionario vacío llamado:

   ```python
   calificaciones = {}
   ```

2. Crea un **menú** con las siguientes opciones:

   ```
   === MENÚ DE CALIFICACIONES ===
   1. Registrar nuevo alumno
   2. Registrar calificaciones para un alumno
   3. Mostrar todas las calificaciones
   4. Salir
   ```

3. **Opción 1: Registrar nuevo alumno**
   - Pide el nombre del alumno.
   - Agrega el nombre al diccionario principal con un diccionario vacío dentro:

     ```python
     calificaciones[nombre] = {}
     ```

   - Muestra el mensaje:  
     `Alumno registrado correctamente.`

4. **Opción 2: Registrar calificaciones para un alumno**
   - Pide el nombre del alumno.
   - Si el alumno no existe, muestra: `Alumno no encontrado.`
   - Si sí existe:
     - Pide el nombre de la materia.
     - Pide la calificación (como número entero o decimal).
     - Agrega la materia y la calificación al diccionario del alumno:

       ```python
       calificaciones[nombre][materia] = calificacion
       ```

     - Permite registrar **varias materias** hasta que el usuario escriba `"salir"`.

5. **Opción 3: Mostrar todas las calificaciones**
   - Recorre el diccionario y muestra los alumnos, sus materias y calificaciones.
   - Calcula el **promedio por alumno** y muéstralo debajo de sus materias.

6. **Opción 4: Salir**
   - Termina el programa mostrando un mensaje de despedida.

---

## 💡 Pistas

- Usa un bucle `while True` para mantener el menú activo.
- Convierte las calificaciones a `int` o `float`.
- Usa `break` para salir del programa.
- Usa `.items()` para recorrer los diccionarios.

---

## 🧩 Ejemplo de funcionamiento

```
=== MENÚ DE CALIFICACIONES ===
1. Registrar nuevo alumno
2. Registrar calificaciones para un alumno
3. Mostrar todas las calificaciones
4. Salir
Elige una opción: 1

Ingresa el nombre del alumno: Emiliano
Alumno registrado correctamente.

Elige una opción: 2
Ingresa el nombre del alumno: Emiliano
Ingresa la materia (o 'salir' para terminar): Matemáticas
Ingresa la calificación: 95
Ingresa la materia (o 'salir' para terminar): Historia
Ingresa la calificación: 88
Ingresa la materia (o 'salir' para terminar): salir

Elige una opción: 3

Emiliano:
  Matemáticas: 95
  Historia: 88
  Promedio: 91.5
```

---