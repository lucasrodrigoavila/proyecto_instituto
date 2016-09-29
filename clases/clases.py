

























class Alumno(Persona):
    def __init__(self, materiaquecursa, aniodeingreso, matricula):
        Persona.__init__(self, nombre, apellido, dni, sexo)
        
            self.materiaquecursa=materiaquecursa
            self.aniodeingreso=aniodeingreso
            self.matricula=matricula
       
    def notasdemateria(self):
        print("Se pide las ", self.materiaquecursa, "el alumno")



class Examen():
	def __init__(self, fecha,aula):
		self.fecha=fecha
		self.aula=aula
		

