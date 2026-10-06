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