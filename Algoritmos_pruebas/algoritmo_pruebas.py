"""
Algoritmo de prueba - EPS
Valida si un afiliado tiene derecho a agendar una cita médica.
Simula la lógica básica del microservicio ms-afiliados / ms-citas.
"""

# Base de datos simulada de afiliados
AFILIADOS = {
    "1001": {"nombre": "Ana Pérez", "estado": "activo"},
    "1002": {"nombre": "Luis Gómez", "estado": "suspendido"},
    "1003": {"nombre": "Marta Ríos", "estado": "activo"},
}


def puede_agendar_cita(documento):
    """Devuelve (True/False, mensaje) según el estado del afiliado."""
    afiliado = AFILIADOS.get(documento)
    if afiliado is None:
        return False, "Afiliado no encontrado"
    if afiliado["estado"] != "activo":
        return False, f"{afiliado['nombre']}: afiliación {afiliado['estado']}"
    return True, f"{afiliado['nombre']}: puede agendar la cita"


if __name__ == "__main__":
    for doc in ["1001", "1002", "9999"]:
        ok, mensaje = puede_agendar_cita(doc)
        print(f"Documento {doc} -> {'OK' if ok else 'RECHAZADO'} | {mensaje}")
