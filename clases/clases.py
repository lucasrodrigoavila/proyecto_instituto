
















class Profesor(Persona):
    
    def __init__(self, materia, estudios, asistencia):
        Persona.__init__(self, nombre, apellido,dni, sexo)
    
            self.materia=materia
            self.estudios=estudios
            self.asistencia=asistencia

    def tomarasistencia(self):
                return self.asistencia





class Examen():
	def __init__(self, fecha,aula):
		self.fecha=fecha
		self.aula=aula
		

