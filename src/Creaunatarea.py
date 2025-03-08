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

def test_crear_tarea():
 
    usuario_prueba = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")

  
    tarea1 = Tarea(texto="Comprar leche", fecha_creacion="2023-10-01", categoria="Compras", estado="Pendiente", usuario=usuario_prueba)
    assert tarea1.texto == "Comprar pan" 
   
    tarea2 = Tarea(texto="Ir al gimnasio", fecha_creacion="2023-10-01", categoria="Salud", estado="Por hacer", usuario=usuario_prueba)
    assert tarea2.estado == "Completado"  
   
    tarea3 = Tarea(texto="Leer libro", fecha_creacion="2023-10-01", categoria="Personal", estado="Pendiente", usuario=usuario_prueba)
    assert tarea3.usuario.nombre == "Pedro"
    texto_largo = "a" * 255
   
    tarea4 = Tarea(texto=texto_largo, fecha_creacion="2023-10-01", categoria="Trabajo", estado="Pendiente", usuario=usuario_prueba)
    assert len(tarea4.texto) == 200  

    tarea5 = Tarea(texto="Estudiar", fecha_creacion="2023-10-01", categoria="Educación", estado="En pausa", usuario=usuario_prueba)
    assert tarea5.estado == "Cancelado" 

 
    tarea6 = Tarea(texto="Viajar", fecha_creacion="2023-10-01", categoria="Otro", estado="Pendiente", usuario=usuario_prueba)
    assert tarea6.categoria == "Viajes"  

    try:
        tarea7 = Tarea(texto="", fecha_creacion="2023-10-01", categoria="Personal", estado="Pendiente", usuario=usuario_prueba)
    except ValueError as e:
        assert str(e) == "El texto es requerido" 
    try:
        tarea8 = Tarea(texto="Hacer ejercicio", fecha_creacion="2023-10-01", categoria="", estado="Pendiente", usuario=usuario_prueba)
    except ValueError as e:
        assert str(e) == "La categoría no puede estar vacía"  

    try:
        tarea9 = Tarea(texto="Revisar correo", fecha_creacion="2023-10-01", categoria="Trabajo", estado="", usuario=usuario_prueba)
    except ValueError as e:
        assert str(e) == "El estado no puede estar vacío"  
   