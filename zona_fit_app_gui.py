import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from zona_fit_gui.cliente import Cliente
from zona_fit_gui.clienteDAO import ClienteDAO


class App(tk.Tk):
	COLOR_VENTANA = '#1d2d44'
	
	def __init__(self):
		super().__init__()
		self.id_cliente = None
		self.configurar_ventana()
		self.configurar_grid()
		self.mostrar_titulo()
		self.mostrar_formulario()
		self.cargar_tabla()
		self.mostrar_botones()
	
	def configurar_ventana(self):
		self.geometry('700x500')  # Tamañp de la ventana
		self.title('Zona Fit App')  # Título
		self.configure(background=App.COLOR_VENTANA)  # Color de fondo
		# Aplicamos el estilo
		self.estilos = ttk.Style()
		self.estilos.theme_use('clam')  # Preparamos los estilos para el modo oscuro
		self.estilos.configure('Dark.TEntry',
		                       foreground='white',
		                       fieldbackground='black',
		                       background='black',
		                       insertcolor='white')  # El color del cursor
		self.estilos.configure('Dark.TFrame', background=App.COLOR_VENTANA)
		self.estilos.configure('TLabel', background=App.COLOR_VENTANA, foreground='white')
	
	def configurar_grid(self):
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
	
	def mostrar_titulo(self):
		etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
		                     font=('Arial', 20),
		                     background=App.COLOR_VENTANA,
		                     foreground='white',
		                     anchor='center')
		etiqueta.grid(row=0, column=0, columnspan=2, pady=30)
	
	def mostrar_formulario(self):
		# Definimos un frame
		self.frame_forma = ttk.Frame(self, style='Dark.TFrame')
		# Definimos el campo de nombre con la etiqueta y la caja de texto
		nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
		nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
		self.nombre_t = ttk.Entry(self.frame_forma, style='Dark.TEntry')
		self.nombre_t.grid(row=0, column=1)
		# Definimos el campo de apellido con la etiqueta y la caja de texto
		apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
		apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
		self.apellido_t = ttk.Entry(self.frame_forma, style='Dark.TEntry')
		self.apellido_t.grid(row=1, column=1)
		# Definimos el campo de membresía con la etiqueta y la caja de texto
		membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
		membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
		self.membresia_t = ttk.Entry(self.frame_forma, style='Dark.TEntry')
		self.membresia_t.grid(row=2, column=1)
		# Publicamos el frame del formulario
		self.frame_forma.grid(row=1, column=0)
	
	def cargar_tabla(self):
		# Creamos un frame para mostrar la tabla
		self.frame_tabla = ttk.Frame(self, style='Dark.TFrame')
		# Definimos los estilos de la tabla
		self.estilos.configure('Treeview', background='black',
		                       foreground='white',
		                       fieldbackground='black',
		                       rowheight=20)
		# Definimos las columnas:
		columnas = ('Id', 'Nombre', 'Apellido', 'Membresia')
		# Creamos el objeto tabla
		self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas,
		                          show='headings')
		# Agregamos los cabeceros
		self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
		self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
		self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
		self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)
		# Definimos las columnas
		self.tabla.column('Id', anchor=tk.CENTER, width=50)
		self.tabla.column('Nombre', anchor=tk.W, width=100)
		self.tabla.column('Apellido', anchor=tk.W, width=100)
		self.tabla.column('Membresia', anchor=tk.W, width=100)
		# Cargar los datos de la base de datos
		try:
			clientes = ClienteDAO.seleccionar()
			for cliente in clientes:
				self.tabla.insert(parent='', index=tk.END,
				                  values=(cliente.idcliente, cliente.nombre,
				                          cliente.apellido, cliente.membresia))
		except Exception as e:
			print(f'Error al cargar los clientes: {e}')
		# Agregamos el scrollbar
		scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
		                          command=self.tabla.yview())
		self.tabla.configure(yscroll=scrollbar.set)
		scrollbar.grid(row=0, column=1, sticky=tk.NS)
		# Asocianos el evento select a la tabla para que al pulsar sobre un registro
		# se carguen esos datos en las cajas de texto y podamos modificarlos
		self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)
		# Publicamos la tabla
		self.tabla.grid(row=0, column=0)
		# Mostramos el frame de tabla
		self.frame_tabla.grid(row=1, column=1, padx=20)
	
	def mostrar_botones(self):
		self.frame_botones = ttk.Frame(self, style='Dark.TFrame')
		# Creamos los botones dentro del frame
		# Botón de agregar
		boton_agregar = ttk.Button(self.frame_botones, text='Guardar',
		                           command=self.validar_cliente)
		boton_agregar.grid(row=0, column=0, padx=30)
		# Botón de eliminar
		boton_eliminar = ttk.Button(self.frame_botones, text='Eliminar',
		                            command=self.eliminar_cliente)
		boton_eliminar.grid(row=0, column=1, padx=30)
		# Botón de limpiar
		boton_limpiar = ttk.Button(self.frame_botones, text='Limpiar',
		                           command=self.limpiar_datos)
		boton_limpiar.grid(row=0, column=2, padx=30)
		
		# Aplicar estilo a los botones
		self.estilos.configure('TButton', background='#005f73')
		self.estilos.map('TButton', background=[('active', '#0a9396')])
		# Publicar el frame de botones
		self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)
	
	def validar_cliente(self):
		# Validar los campos
		if (self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
			if self.validar_membresia():
				self.guardar_cliente()
			else:
				showerror(title='Atención',
				          message='El valor de membresía tiene que ser numérico')
				# Si membresía no es un valor numérico, limpiamos el campo
				self.membresia_t.delete(0, tk.END)
				# Ponemos el cursor sobre el campo membresía para que el usuario pueda llenar de nuevo el valor
				self.membresia_t.focus_set()
		else:
			showerror(title='Atencion',
			          message='Debe rellenar el formulario completo')
			# Ponemos el fooc en el campo de nombre
			self.nombre_t.focus_set()
	
	def validar_membresia(self):
		try:
			int(self.membresia_t.get())
			return True
		except:
			return False
	
	def guardar_cliente(self):
		# Recuperar los valores de las cajas ed textp
		nombre = self.nombre_t.get()
		apellido = self.apellido_t.get()
		membresia = self.membresia_t.get()
		# Validamos el valor de id_cliente
		if self.id_cliente is None:
			cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
			ClienteDAO.insertar(cliente)
			showinfo(title='Agregar', message='Cliente agregado')
		else:  # Actualizar el registro
			cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
			ClienteDAO.actualizar(cliente)
			showinfo(title='Actualizar', message='Cliente actualizado')
		# Volvemos a mostrar los datos y limpiamos el formulario
		self.recargar_datos()
	
	def cargar_cliente(self, event):
		elemento_seleccionado = self.tabla.selection()[0]
		elemento = self.tabla.item(elemento_seleccionado)
		# Recuperamos la tupla de valores del elemento seleccionado
		cliente_t = elemento['values']
		# Recuperar cada valor del cliente
		self.id_cliente = cliente_t[0]
		nombre = cliente_t[1]
		apellido = cliente_t[2]
		membresia = cliente_t[3]
		# Limpiamos el formulario antes de cargar estos datos
		self.limpiar_formulario()
		# Cargamos los valoes en el formulario
		self.nombre_t.insert(0, nombre)
		self.apellido_t.insert(0, apellido)
		self.membresia_t.insert(0, membresia)
	
	def recargar_datos(self):
		# Volver a cargar los datos de la tabla
		# Tiene que regenerar la tabla con la nueva información de la base de datos
		self.cargar_tabla()
		# Limpiar los datos
		self.limpiar_datos()
	
	def eliminar_cliente(self):
		# Tiene que haberse seleccionado un cliente, por tanto id_cliente tiene
		# que ser distinto de None
		if self.id_cliente is None:
			showerror(title='Atención',
			          message='Debe seleccionar un cleinte a eliminar')
		else:
			cliente = Cliente(idcliente=self.id_cliente)
			ClienteDAO.eliminar(cliente)
			showinfo(title='Eliminar', message='Cliente eliminado')
			self.recargar_datos()
	
	def limpiar_datos(self):
		self.limpiar_formulario()
		# Reestablecemos el valor de id_cliente cada vez que limpiemos el formulario
		self.id_cliente = None
	
	def limpiar_formulario(self):
		self.nombre_t.delete(0, tk.END)
		self.apellido_t.delete(0, tk.END)
		self.membresia_t.delete(0, tk.END)


if __name__ == '__main__':
	app = App()
	app.mainloop()
