from zona_fit_gui.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
	SELECCIONAR = 'SELECT * FROM cliente ORDER BY idcliente'
	INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
	ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE idcliente=%s'
	ELIMINAR = 'DELETE FROM cliente WHERE idcliente=%s'
	
	@classmethod
	def seleccionar(cls):
		conexion = None
		cursor = None
		try:
			conexion = Conexion.obtener_conexion()
			cursor = conexion.cursor()
			cursor.execute(cls.SELECCIONAR)
			registros = cursor.fetchall()
			clientes = []
			for registro in registros:
				cliente = Cliente(registro[0], registro[1],
				                  registro[2], registro[3])
				clientes.append(cliente)
			return clientes
		except Exception as e:
			print(f'Ha ocurrido la excepcion {e}')
		finally:
			if conexion is not None:
				cursor.close()
				Conexion.liberar_conexion(conexion)
	
	@classmethod
	def insertar(cls, cliente):
		conexion = None
		cursor = None
		try:
			conexion = Conexion.obtener_conexion()
			cursor = conexion.cursor()
			valores = (cliente.nombre, cliente.apellido, cliente.membresia)
			cursor.execute(cls.INSERTAR, valores)
			conexion.commit()
			return cursor.rowcount
		except Exception as e:
			print(f'Ha ocurrido un error al insertar un cliente: {e}')
		finally:
			if cursor is not None:
				cursor.close()
				Conexion.liberar_conexion(conexion)
	
	@classmethod
	def actualizar(cls, cliente):
		conexion = None
		cursor = None
		try:
			conexion = Conexion.obtener_conexion()
			cursor = conexion.cursor()
			valores = (cliente.nombre, cliente.apellido,
			           cliente.membresia, cliente.idcliente)
			cursor.execute(cls.ACTUALIZAR, valores)
			conexion.commit()
			return cursor.rowcount
		except Exception as e:
			print(f'Error al actualizar el cliente: {e}')
		finally:
			if conexion is not None:
				cursor.close()
				Conexion.liberar_conexion(conexion)
	
	@classmethod
	def eliminar(cls, cliente):
		conexion = None
		cursor = None
		try:
			conexion = Conexion.obtener_conexion()
			cursor = conexion.cursor()
			valores = (cliente.idcliente,)
			cursor.execute(cls.ELIMINAR, valores)
			conexion.commit()
			return cursor.rowcount
		except Exception as e:
			print(f'Error al intentar eliminar el cliente: {e}')
		finally:
			if conexion is not None:
				cursor.close()
				Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
	# Insertar clientes
	# cliente1 = Cliente(nombre='Alejandra', apellido='Tevez', membresia=250)
	# clientes_insertados = ClienteDAO.insertar(cliente1)
	# print(f'Clientes insertados: {clientes_insertados}')
	# Actualizar cliente:
	# cliente_actualizar = Cliente(3, 'Alexa', 'Tomeroso', 220)
	# clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
	# print(f'Clientes actualizados: {clientes_actualizados}')
	# Eliminar cliente
	cliente_eliminar = Cliente(idcliente=4)
	clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
	print(f'Clientes eliminados: {clientes_eliminados}')
	clientes = ClienteDAO.seleccionar()
	for cliente in clientes:
		print(cliente)
