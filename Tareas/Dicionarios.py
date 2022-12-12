persona={"Nombre":"Jarison","Apellidos":"Mican","edad":14,"sueldo":100.000}
print(persona)
print(persona["Nombre"])
#actualizar
persona["edad"]=40
print(persona)
#eliminar
del persona["sueldo"]
print(persona)
#get si no encuentra  ninguno
print(persona.get("Nombre","Ninguno"))