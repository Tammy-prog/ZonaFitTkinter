class Cliente:
	def __init__(self, idcliente=None, nombre=None, apellido=None, membresia=None):
		self.idcliente = idcliente
		self.nombre = nombre
		self.apellido = apellido
		self.membresia = membresia
	
	def __str__(self):
		return (f'Id: {self.idcliente}, Nombre: {self.nombre},'
		        f'Apellido: {self.apellido}, Membresía: {self.membresia}')
