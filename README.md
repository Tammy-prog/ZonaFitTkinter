# ZonaFitTkinter 🏋️‍♀️ App
Aplicación de escritorio desarrollada en Python con `tkinter` para gestionar clientes de un gimnasio.

## Funcionalidades

✅ Agregar nuevos clientes  
✅ Editar información de clientes  
✅ Eliminar clientes existentes  
✅ Visualizar clientes en una tabla  
✅ Validación de entradas y estilos oscuros

## Tecnologías utilizadas

- Python 3
- tkinter (interfaz gráfica)
- ttk (widgets estilizados)
- SQLite (usado desde `clienteDAO.py`, asumiendo una base de datos simple)

## Estructura del proyecto

zona-fit-app/
├── app.py # Ventana principal con interfaz
├── zona_fit_gui/
│ ├── cliente.py # Clase Cliente
│ ├── clienteDAO.py # Operaciones CRUD con la base de datos


