# Diagnóstico y Exploración Inicial NoSQL - Caso TecnoServicios

Este repositorio contiene la solución completa y las evidencias correspondientes a la **Semana 1 / Actividad A4** del módulo de **Bases de Datos NoSQL**. En este laboratorio inicial se evaluaron los fundamentos teóricos, la selección de modelos de datos, la formulación de reglas de negocio y la integración práctica de **MongoDB** mediante script de exploraciones e inspección visual.

---

##  Contexto del Proyecto

**TecnoServicios** es un taller de soporte técnico especializado en el mantenimiento de portátiles, teléfonos móviles y tabletas. Debido al crecimiento de sus operaciones, el taller requiere migrar su gestión de hojas de cálculo a un modelo documental NoSQL que permita gestionar equipos con especificaciones heterogéneas, rastrear historiales de reparación y asegurar el cumplimiento de compromisos de entrega sin la rigidez de esquemas tabulares tradicionales.

---

##  Lo Desarrollado en la Actividad

### 1. Selección y Comparación de Modelos NoSQL (`A2`)
Se realizó un análisis comparativo entre modelos Relacionales (SQL) y NoSQL (Documental, Clave-Valor, Grafos y Series de Tiempo) para determinar el caso de uso óptimo en el taller, identificando los límites de cada paradigma y estableciendo los criterios claros para conservar SQL cuando se requiera consistencia financiera o transaccional estricta.

### 2. Definición de Requisitos y Consultas Clave (`A3`)
Se estructuraron las **6 consultas clave (Q01–Q06)** necesarias para la operación diaria de TecnoServicios, estableciendo actores, filtros, ordenamientos y frecuencias de ejecución, acompañadas de las reglas de negocio indispensables del taller:
* **Unicidad:** Códigos de equipos y números de orden únicos.
* **Flujo de Estados:** `recibida` $\rightarrow$ `en_diagnostico` $\rightarrow$ `en_reparacion` $\rightarrow$ `lista_entrega` $\rightarrow$ (`cerrada` | `cancelada`).
* **Límite de Concurrencia:** Máximo una (1) orden activa por equipo a la vez.
* **Integridad Temporal:** Fechas BSON nativas (`ISODate`) para validaciones de rangos y compromisos.

### 3. Implementación Práctica y Conexión (`01_explorar.mongodb.js`)
Se desarrolló y probó el script de inserción y exploración en **MongoDB** utilizando la sintaxis nativa de *VS Code Playgrounds*:
* Creación e instanciación de la base de datos `tecnoservicios_db` y colección `ordenes_demo`.
* Inserción de documentos BSON con subdocumentos anidados (`cliente` y `equipo`).
* Uso del tipo de dato `ISODate()` nativo y su posterior validación programática en código.
* Confirmación de datos y estructura a través de **MongoDB Compass**.

---

##  Estructura del Repositorio

```text
diagnostico_nosql/
├── evidencias/                # Capturas de pantalla e inspección visual en Compass
├── scripts/
│   ├── 01_explorar.mongodb.js  # Script ejecutable en VS Code (Playground)
│   ├── A2_matriz_modelos.md   # Matriz comparativa de paradigmas NoSQL vs SQL
│   └── A3_Q01-Q06_reglas.md   # Especificación de consultas Q01-Q06 y reglas de negocio
├── P1_json.py                 # Diagnóstico inicial Python / JSON
├── P2_python.py               # Script de filtrado en estructuras de datos
├── P3_sql.py                  # Evaluación de relaciones en SQLite
└── README.md                  # Documentación general del laboratorio

```

## DGN-01. DIAGNÓSTICO INDIVIDUAL Bases de Datos NoSQL – Semana 1

Diagnóstico, fundamentos y entorno de trabajo Caso integrador: TecnoServicios — gestión de equipos y órdenes de reparación
Aprendiz
Thomas Isaza
Programa
Tecnología en Análisis y Desarrollo de Software — ADSO
Centro / instructor
CTMA / Wilson Castro Gil
Actividad
Bases de Datos NoSQL — Semana 1
Fecha
06 de octubre de 2026

---

## A1. Diagnóstico teórico

## 1. ¿Qué representan una tabla, una fila y una clave primaria? Utiliza un ejemplo relacionado con los equipos del taller.

Una tabla representa una estructura organizada para almacenar información sobre una entidad o concepto.
Una fila representa un registro o una instancia concreta de esa entidad.
La clave Primaria es un campo, o conjunto de campos, que identifica de manera única cada registro y evita duplicidades.
Ejemplo: una tabla llamada equipos puede contener los campos (codigo, tipo y numero_serie). Cada fila corresponde a un equipo del taller y el campo codigo puede utilizarse como clave primaria, siempre que sea único y no nulo.

## 2. ¿Para qué sirve una clave foránea? ¿Qué problema genera una orden que referencia a un cliente inexistente?

Una clave foránea sirve para establecer una relación entre registros de dos tablas y mantener la integridad referencial. Por ejemplo, una tabla ordenes puede tener cliente_id que referencia al id de la tabla clientes.
Si una orden referencia a un cliente que no existe, se genera una inconsistencia en los datos. Si existe una restricción de clave foránea, la base de datos puede rechazar esa operación; sin dicha restricción, podría quedar una referencia sin correspondencia válida.

## 3. Explica qué devuelve SELECT codigo FROM equipos WHERE tipo = 'portatil';. ¿Modifica registros?
La consulta selecciona y devuelve el campo codigo de los registros de la tabla equipos cuyo campo tipo sea exactamente 'portatil'. Es una operación de lectura y no modifica, elimina ni inserta registros.

## 4. Diferencia una lista y un diccionario en Python. ¿Qué estructura utilizarías para un equipo y para varios equipos?
Una lista es una colección ordenada de elementos y se representa normalmente con corchetes. Un diccionario almacena información mediante pares clave-valor y se representa con llaves. Para representar un solo equipo utilizaría un diccionario, por ejemplo: {'codigo': 'EQ-001', 'tipo': 'portatil'}. Para representar varios equipos utilizaría una lista de diccionarios, donde cada diccionario representa un equipo.

## 5. ¿Son equivalentes false y "false" en JSON? Explica el tipo de cada valor.
No son equivalentes. false es un valor booleano cuyo valor lógico es falso. En cambio, "false" es una cadena de texto que contiene los caracteres de string. Por lo tanto, sus tipos son diferentes: booleano frente a cadena de texto. En JSON, los valores booleanos se escriben como true y false, sin comillas.

## 6. Diferencia un campo ausente, un campo con null y un campo con una cadena vacía. Propón un ejemplo.
Un campo ausente significa que la clave no existe en el documento. Un campo con null significa que la clave existe y tiene explícitamente el valor nulo. Una cadena vacía es un valor de texto existente cuya longitud es cero. Ejemplo: { } representa un campo ausente.
{'fecha_cierre': null} representa un campo presente con valor nulo.
{'observacion': ''} representa una cadena vacía.
No deben tratarse automáticamente como equivalentes, porque cada situación puede tener un significado diferente según las reglas del Sistema o contexto.

## 7. ¿Qué ventaja tiene una función que retorna datos frente a otra que únicamente los imprime?
Una función que retorna datos permite que el resultado sea utilizado posteriormente por otra parte del programa: puede almacenarse en una variable, validarse, transformarse, combinarse con otros resultados o utilizarse en pruebas. Una función que únicamente imprime está orientada a mostrar información en pantalla y su resultado no queda disponible directamente para que el programa lo reutilice.

## 8. Si falla la lectura de un archivo JSON, ¿qué revisarías antes de cambiar el programa?
Primero revisaría el mensaje exacto del error y la ubicación donde se produce. También comprobaría que la ruta y el nombre del archivo sean correctos, que el archivo exista y que haya permisos de lectura. Después revisaría la sintaxis JSON: uso de comillas dobles, llaves y corchetes correctamente cerrados, valores válidos y ausencia de comas finales no permitidas. Antes de modificar el programa, intentaría determinar si el problema está realmente en el archivo o en la forma de acceder a él.

## 9. ¿Qué información reconoces en 2026-10-06T13:00:00Z? ¿Qué ambigüedades evita frente a 06/10/26 8:00?
Se utiliza un formato de fecha y hora. Indica el año 2026, mes 10, día 06, hora 13:00 y la letra Z (Dentro de mis conocimientos no comprendia realmente que significaba pero al investigantar) indica que el instante está expresado en UTC. En Colombia corresponde a las 08:00. Frente a '06/10/26 8:00', el formato ISO evita ambigüedades sobre el orden de año, mes y día, utiliza una representación explícita de la hora y, principalmente, especifica la zona de referencia mediante Z. Esto permite identificar un instante de manera inequívoca.

## 10. Se publicó por error una contraseña en Git. ¿Qué acciones propondrías? ¿Es suficiente borrarla del archivo actual?
No es suficiente con borrarla del archivo actual, porque la contraseña puede permanecer en el historial de Git y considerarse expuesta. La primera acción debe ser invalidar o cambiar la contraseña afectada y notificar el incidente según el procedimiento del proyecto. Después se debe eliminar el secreto del lugar donde fue publicado y, cuando corresponda, corregir el historial del repositorio siguiendo el procedimiento establecido. También se debe evitar volver a almacenar credenciales en el código, utilizando variables de entorno o un mecanismo de gestión de secretos. El archivo .gitignore ayuda a evitar nuevos archivos sensibles, pero no elimina una credencial que ya fue versionada.
