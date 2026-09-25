#ejercicio 1 imprimir el nombre y edad y materia favorita de un alumno

nombre = input("Ingrese su nombre: ")
materia = input("Ingrese su materia favorita: ")
edad = int(input("Ingrese su edad: "))

print("Nombre:", nombre)
print("Materia favorita:", materia)
print("Edad:", edad)




alumnos = [
{
"nombre": "Juan",
"materia": "Programacion",
"edad": 16
},
{
"nombre": "Maria",
"materia": "Matematica",
"edad": 17
},
{
"nombre": "pepe",
"materia": "Programación",
"edad": 59
}

]
for alumno in alumnos:
    print(alumno["nombre"], alumno["materia"], alumno["edad"])
