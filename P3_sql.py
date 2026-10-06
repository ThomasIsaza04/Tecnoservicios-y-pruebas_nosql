import sqlite3

conexion = sqlite3.connect(":memory:")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY,
        alias TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE ordenes (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER NOT NULL,
        estado TEXT NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
""")

clientes = [
    (1, "cliente_ana"),
    (2, "cliente_luis"),
    (3, "cliente_maria")
]

ordenes = [
    (101, 1, "recibida"),
    (102, 2, "en_reparacion"),
    (103, 3, "recibida"),
    (104, 1, "entregada")
]

cursor.executemany(
    "INSERT INTO clientes (id, alias) VALUES (?, ?)",
    clientes
)

cursor.executemany(
    "INSERT INTO ordenes (id, cliente_id, estado) VALUES (?, ?, ?)",
    ordenes
)

conexion.commit()

cursor.execute("""
    SELECT ordenes.id, clientes.alias
    FROM ordenes
    INNER JOIN clientes
        ON ordenes.cliente_id = clientes.id
    WHERE ordenes.estado = ?
    ORDER BY ordenes.id
""", ("recibida",))

resultados = cursor.fetchall()

print("Órdenes recibidas:")

for orden_id, alias in resultados:
    print(f"Orden: {orden_id} - Cliente: {alias}")

cursor.close()
conexion.close()