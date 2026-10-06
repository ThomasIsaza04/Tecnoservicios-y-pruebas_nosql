# Actividad A2: Comparación de Necesidades y Familias NoSQL
**Caso Integrador:** TecnoServicios  
**Evidencia:** E01 - Matriz de Selección de Modelos  

---

## Matriz Comparativa de Modelos de Bases de Datos

| Caso / Necesidad | Modelo Propuesto | Razón Vinculada a una Consulta | Límite o Costo | Situación en la que Conservaría SQL |
| :--- | :--- | :--- | :--- | :--- |
| **Catálogo de dispositivos** | **Documental** *(ej. MongoDB)* | Permite consultar y almacenar equipos con especificaciones heterogéneas *(portátiles, teléfonos, tablets)* sin campos nulos o columnas vacías. | Menor estandarización; requiere validaciones estrictas a nivel de aplicación o mediante JSON Schema. | Cuando las especificaciones de los dispositivos sean fijas e invariables y requieran relaciones tabulares estrictas con inventario de repuestos. |
| **Sesiones temporales** | **Clave-Valor** *(ej. Redis)* | Búsqueda ultrarrápida por clave única *(ej. `session_id`)* con expiración automática mediante TTL *(Time-To-Live)*. | Funcionalidad de consulta muy limitada; no permite filtrado eficiente por atributos complejos o subdocumentos. | Cuando la sesión deba registrarse de forma auditable e inmutable dentro de un historial de auditoría en tablas SQL. |
| **Recorridos de relaciones** | **Grafos** *(ej. Neo4j)* | Consulta eficiente de relaciones en red *(recorridos entre técnicos, habilidades, certificaciones y servicios asignados)*. | Costo computacional elevado para agregaciones numéricas masivas o consultas CRUD tradicionales. | Cuando solo exista una relación jerárquica simple 1:N *(ej. un cliente tiene N órdenes de servicio)*. |
| **Lecturas por dispositivo / periodo** | **Familias de Columnas / Series de Tiempo** *(ej. Cassandra / InfluxDB)* | Optimizado para altísima tasa de escritura y lecturas masivas por rangos de tiempo continuo *(telemetría/bancos de prueba)*. | Alta complejidad de administración en clúster y modelo de datos rígido orientado a consultas predefinidas. | Cuando el volumen de métricas sea bajo y se requieran reportes consolidados mensuales en una BD transaccional. |

---

