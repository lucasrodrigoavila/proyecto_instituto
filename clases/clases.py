

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


class Alumno(Persona):
    def __init__(self, materiaquecursa, aniodeingreso, matricula):
        Persona.__init__(self, nombre, apellido, dni, sexo)
        
            self.materiaquecursa=materiaquecursa
            self.aniodeingreso=aniodeingreso
            self.matricula=matricula
       
    def notasdemateria(self):
        print("Se pide las ", self.materiaquecursa, "el alumno")

class Profesor(Persona):
    
    def __init__(self, materia, estudios, asistencia):
        Persona.__init__(self, nombre, apellido,dni, sexo)
    
            self.materia=materia
            self.estudios=estudios
            self.asistencia=asistencia

    def tomarasistencia(self):
                return self.asistencia


class Examen(profesor,alumno):
	def __init__(self, fecha,aula):
		self.fecha=fecha
		self.aula=aula
		

