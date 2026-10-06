# import json

# texto = '{"codigo":"OS-001", "prioritaria":True, "fallas":["No enciende",]}'

# datos = json.loads(texto)

# print(datos)
import json

texto = '{"codigo":"OS-001", "prioritaria":true, "fallas":["No enciende"]}'

datos = json.loads(texto)

print(datos)

print("codigo:", datos["codigo"])
print("prioritaria:", datos["prioritaria"])
print("tipo codigo:", type(datos["codigo"]).__name__)
print("tipo prioritaria:", type(datos["prioritaria"]).__name__)