registros = [
    {
        "codigo": "OS-001",
        "prioridad": "alta",
        "pendiente": True
    },
    {
        "codigo": "OS-002",
        "prioridad": "media",
        "pendiente": True
    },
    {
        "codigo": "OS-003",
        "prioridad": "alta",
        "pendiente": False
    },
    {
        "codigo": "OS-004",
        "prioridad": "alta",
    }
]


def seleccionar_pendientes(registros, prioridad):
    resultados = []

    for registro in registros:
        if registro.get("prioridad") == prioridad and registro.get("pendiente") is True:
            resultados.append(registro["codigo"])

    return resultados


# Prueba 1: debe encontrar resultados
resultado1 = seleccionar_pendientes(registros, "alta")
print("Pendientes de prioridad alta:", resultado1)


# Prueba 2: no debe encontrar resultados
resultado2 = seleccionar_pendientes(registros, "baja")
print("Pendientes de prioridad baja:", resultado2)