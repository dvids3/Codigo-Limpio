from Usuario import Usuario
from tarea import Tarea

def test_crear_tarea():
    # Crear una instancia de Usuario
    usuario_prueba = Usuario(nombre="Juan", id=1)

    # Crear una instancia de Tarea
    tarea_prueba = Tarea(
        texto="Comprar leche",
        fecha_creacion="2023-10-01",
        categoria="Compras",
        estado="Pendiente",
        usuario=usuario_prueba
    )

    # Verificar que la tarea se haya creado correctamente
    assert tarea_prueba.texto == "Comprar leche"
    assert tarea_prueba.categoria == "Compras"
    assert tarea_prueba.estado == "Pendiente"
    assert tarea_prueba.usuario.nombre == "Juan"
    assert tarea_prueba.usuario.id == 1
