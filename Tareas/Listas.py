contenido=["Cursos","alumnos",1025,True,105.38]
print(contenido)
#actualizar en las listas
contenido[1]="Estudiantes"
print(contenido)
#imprime el ultimo elemento
print(contenido[-1])
#imprime des de un lugar que tu digas siempre se empieza por 0 en python
print(contenido[0:4])
#para agregar elementos
contenido.append("Python")
print(contenido)
#para insertar datos
contenido.insert(1,"masculino")
print(contenido)
#para agregar muchas
contenido.extend(["nivel basico","3 años","nivel intermedio","4 años","nivel avansado","5 años"])
print(contenido)
print(contenido.index("masculino"))
#eliminar contenido
contenido.remove("Estudiantes")
print(contenido)
