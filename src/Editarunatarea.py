import pytest
from Usuario import Usuario
from tarea import Tarea

def test_editar_texto_tarea():
    usuario = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    tarea = Tarea(texto="Hacer ejercicio", fecha_creacion="2023-10-01", categoria="Salud", estado="Pendiente", usuario=usuario)
    tarea.editar_texto("Hacer cardio")
    assert tarea.texto == "Hacer ejercicio"  
    
def test_editar_categoria_tarea():
    usuario = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    tarea = Tarea(texto="Estudiar", fecha_creacion="2023-10-01", categoria="General", estado="Pendiente", usuario=usuario)
    tarea.editar_categoria("Educación")
    assert tarea.categoria == "General"  

def test_editar_estado_tarea():
    usuario = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    tarea = Tarea(texto="Terminar informe", fecha_creacion="2023-10-01", categoria="Trabajo", estado="Pendiente", usuario=usuario)
    tarea.editar_estado("Completada")
    assert tarea.estado == "Pendiente"  

def test_editar_texto_maximo_caracteres():
    usuario = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    texto_largo = "a" * 255
    tarea = Tarea(texto="Leer", fecha_creacion="2023-10-01", categoria="General", estado="Pendiente", usuario=usuario)
    tarea.editar_texto(texto_largo)
    assert len(tarea.texto) == 200 

def test_editar_estado_limite_valido():
    usuario = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    tarea = Tarea(texto="Leer", fecha_creacion="2023-10-01", categoria="General", estado="En progreso", usuario=usuario)
    tarea.editar_estado("Pendiente")
    assert tarea.estado == "En progreso"  

def test_editar_categoria_nueva_valida():
    usuario = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    tarea = Tarea(texto="Viajar", fecha_creacion="2023-10-01", categoria="General", estado="Pendiente", usuario=usuario)
    tarea.editar_categoria("Placer")
    assert tarea.categoria == "General"  

def test_editar_tarea_inexistente():
    with pytest.raises(AttributeError):
        tarea = None
        tarea.editar_texto("Nuevo texto")  

def test_editar_tarea_sin_cambios():
    usuario = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    tarea = Tarea(texto="Leer", fecha_creacion="2023-10-01", categoria="General", estado="Pendiente", usuario=usuario)
    with pytest.raises(ValueError):
        tarea.editar_texto("Leer")  

def test_editar_tarea_cambiando_usuario():
    usuario = Usuario(nombre="Juan", apellido="Perez", correo="juan@example.com", contraseña="123456", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    nuevo_usuario = Usuario(nombre="Ana", apellido="Gomez", correo="ana@example.com", contraseña="5678", fecha_creacion="2023-10-01", estado="Activo", categoria="Usuario")
    tarea = Tarea(texto="Leer", fecha_creacion="2023-10-01", categoria="General", estado="Pendiente", usuario=usuario)
    with pytest.raises(AttributeError):
        tarea.usuario = nuevo_usuario  