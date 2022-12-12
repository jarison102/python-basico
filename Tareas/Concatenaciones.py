nombre="Jarison"
Apellido="Mican"
Especialidad="Desarrollador de Software"
edad=18
#primera forma de concatenacion
print("Mi nombre es:%s"%nombre)
#Segunda Forma de concatenacion
print("Mi nombre es:%s Mi apellido:%s"%(nombre,Apellido))
#Tercera forma de concatenacion
print("Mi nombre es:{0}y mi especialidad es:{1}y mi edad es:{2}".format(nombre,Especialidad,edad))
#Cuarta forma de concatenacion
print("Mi nombre es:{a}".format(a=nombre))