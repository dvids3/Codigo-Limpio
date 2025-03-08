from Usuario import Usuario

class Tarea:
    def __init__(self, texto, fecha_creacion, categoria, estado, usuario):
        if not texto:
            raise ValueError("El texto no puede estar vacío")
        if not categoria:
            raise ValueError("La categoría es requerida")
        if not estado:
            raise ValueError("El estado es requerido")
        
        self.texto = texto
        self.fecha_creacion = fecha_creacion
        self.categoria = categoria
        self.estado = estado
        self.usuario = usuario

