class Usuario:
    def __init__(self, nombre, apellido, correo, contraseña, fecha_creacion, estado, categoria):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.fecha_creacion = fecha_creacion
        self.estado = estado
        self.categoria = categoria

    def crear_tarea(self, texto, categoria, estado):
        tarea = tarea(texto=texto, categoria=categoria, estado=estado, usuario=self)
        return tarea