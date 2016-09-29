


class Persona:
	def __init__ (self, nombre, apellido, dni, sexo):
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.sexo = sexo

	def nombre(self):
		self.nombre = self.nombre

	def apellido(self):
		self.apellido = self.apellido

	def dni(self):
		self.dni = self.dni

	def sexo(self):
		self.sexo = self.sexo

	def mostrar_listado(self):
		print ("Listado de las Persona",, self.nombre, self.apellido, self.dni, self.sexo)


class Examen():
	def __init__(self, fecha,aula):
		self.fecha=fecha
		self.aula=aula
		

