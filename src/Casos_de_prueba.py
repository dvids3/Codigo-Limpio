from Usuario import Usuario
from tarea import Tarea

def test_crear_tarea_con_texto_y_categoria_validos():
    # Crear una instancia de Usuario
    usuario_prueba = Usuario(
        nombre="Juan",
        apellido="Pérez",
        correo="juan@example.com",
        contraseña="password123",
        fecha_creacion="2023-10-01",
        estado="Activo",
        categoria="Usuario"
    )

    # Crear una tarea con texto y categoría válidos
    tarea_prueba = usuario_prueba.crear_tarea(
        texto="Comprar leche",
        categoria="Compras",
        estado="Pendiente"
    )

    # Verificar que la tarea se haya creado correctamente
    assert tarea_prueba.texto == "Comprar leche"
    assert tarea_prueba.categoria == "Compras"
    assert tarea_prueba.estado == "Pendiente"
    assert tarea_prueba.usuario.nombre == "Juan"
    assert tarea_prueba.usuario.correo == "juan@example.com"