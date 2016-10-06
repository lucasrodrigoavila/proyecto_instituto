from clases import Persona
from clases import Profesor 
from clases import Alumno
from clases import Examen


Pedro=Profesor('juan','perez',1234, 'masc','Etica','Profesorado de Etica','Presente')

Lucas=Alumno('Lucas','Avila',45363,'masc','Redes',2015,12334)

Sonia=Alumno('Sonia','Tapia',78242,'fem','Validacion',2015,4562)

alumnos=[Lucas, Sonia]

martes=Examen('21/09/2017','A', Pedro,alumnos)
martes.mostrar()