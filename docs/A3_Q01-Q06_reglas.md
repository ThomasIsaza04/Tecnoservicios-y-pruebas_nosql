# A3 — Reglas y consultas del caso TecnoServicios

## Propósito

Definir las necesidades de consulta y las reglas del caso **TecnoServicios** antes de diseñar las colecciones.

Esta matriz corresponde a la actividad **A3 — Formular reglas y consultas de TecnoServicios**.

> **Nota:** En esta etapa no es necesario escribir las consultas en MongoDB. Se documentan las necesidades, filtros, salidas, orden y frecuencia estimada.

---

## Q01 — Órdenes pendientes por prioridad y estado

- **Actor:** Personal encargado del seguimiento de órdenes.
- **Filtros:** Prioridad y estado de la orden. Se consideran pendientes las órdenes que estén en estados activos.
- **Campos de salida:** Número de orden, prioridad, estado, código del equipo y fecha de compromiso.
- **Orden:** Por prioridad y fecha de compromiso.
- **Frecuencia estimada:** Alta. Es una hipótesis, no una estadística medida.

---

## Q02 — Detalle de un equipo y sus características técnicas

- **Actor:** Personal técnico o encargado de recepción/diagnóstico.
- **Filtros:** Código identificador del equipo.
- **Campos de salida:** Código del equipo, tipo de equipo y características técnicas.
- **Orden:** No aplica cuando se consulta un único equipo.
- **Frecuencia estimada:** Media/alta. Es una hipótesis, no una estadística medida.

---

## Q03 — Órdenes de un cliente por periodo y estado

- **Actor:** Personal encargado de atención y seguimiento.
- **Filtros:** Cliente, periodo de fechas y estado de la orden.
- **Campos de salida:** Número de orden, código del equipo, estado, fecha de ingreso y fecha de compromiso.
- **Orden:** Por fecha de ingreso, de la más reciente a la más antigua.
- **Frecuencia estimada:** Media. Es una hipótesis, no una estadística medida.

---

## Q04 — Órdenes con compromiso vencido a una fecha de corte

- **Actor:** Personal encargado del seguimiento de órdenes.
- **Filtros:** Fecha de compromiso anterior a la fecha de corte y situación de la orden al momento del corte.
- **Campos de salida:** Número de orden, código del equipo, estado, fecha de ingreso y fecha de compromiso.
- **Orden:** Por fecha de compromiso ascendente.
- **Frecuencia estimada:** Alta. Es una hipótesis, no una estadística medida.

---

## Q05 — Historial de órdenes de un equipo

- **Actor:** Personal técnico o encargado de atención.
- **Filtros:** Código identificador del equipo.
- **Campos de salida:** Número de orden, estado, fecha de ingreso, fecha de compromiso y datos necesarios para identificar el servicio realizado.
- **Orden:** Por fecha de ingreso, de la más antigua a la más reciente.
- **Frecuencia estimada:** Media. Es una hipótesis, no una estadística medida.

---

## Q06 — Cantidad de órdenes por tipo de equipo y mes

- **Actor:** Responsable del seguimiento o análisis del taller.
- **Filtros:** Tipo de equipo y periodo de tiempo.
- **Campos de salida:** Tipo de equipo, mes y cantidad de órdenes.
- **Orden:** Por mes y tipo de equipo.
- **Frecuencia estimada:** Baja/media. Es una hipótesis, no una estadística medida.

---

# Reglas del caso

1. **Código de equipo y número de orden únicos:** deben ser únicos dentro del alcance del taller.

2. **Relación entre orden, equipo y cliente:** cada orden corresponde a un equipo y a un cliente solicitante existente.

3. **Solicitante no equivale automáticamente a propietario:** el cliente que solicita el servicio no debe asumirse automáticamente como propietario del dispositivo.

4. **Estados propuestos:** `recibida`, `en_diagnostico`, `en_reparacion`, `lista_entrega`, `cerrada` y `cancelada`.

5. **Órdenes activas:** se consideran activas las primeras cuatro situaciones: `recibida`, `en_diagnostico`, `en_reparacion` y `lista_entrega`.

6. **Órdenes no pendientes:** las órdenes `cerrada` o `cancelada` no están pendientes.

7. **Fecha de compromiso:** debe ser igual o posterior a la fecha de ingreso.

8. **Fecha de cierre:** si existe una fecha de cierre, no puede ser anterior a la fecha de ingreso.

9. **Una orden activa por equipo:** para simplificar el caso, debe existir como máximo una orden activa por equipo.

10. **Conservación del historial:** el historial debe conservarse aunque un equipo deje de atenderse. Antes de borrar información debe existir una política definida.

11. **Datos sintéticos:** se utilizan códigos y alias ficticios, sin teléfonos, documentos de identidad ni información de dispositivos reales.

12. **Alcance inicial:** contempla recepción, diagnóstico técnico, reparación y seguimiento de órdenes. Facturación, pagos, inventario de repuestos y mensajería quedan fuera del producto inicial.

---

# Preguntas adicionales para el cliente

## Pregunta 1

**¿Qué información del equipo debe conservarse históricamente en cada orden cuando las características actuales del equipo cambien?**

**Propósito:** aclarar qué información debe conservar una orden sobre el estado del equipo en el momento de la recepción.

## Pregunta 2

**¿Qué criterio debe utilizar el taller para considerar una orden como vencida cuando ya fue cerrada o cancelada antes de la fecha de corte?**

**Propósito:** precisar la interpretación de los compromisos vencidos y su comportamiento en consultas históricas.

---

# Riesgo identificado

**Riesgo:** interpretar incorrectamente el estado de una orden al consultar compromisos vencidos.

Una consulta basada únicamente en el estado actual podría producir resultados incorrectos cuando se analiza una fecha de corte histórica. Por eso, Q04 debe considerar la situación de la orden respecto del momento del corte, incluyendo si ya había sido cerrada o cancelada.

---

# Observaciones para el diseño posterior

- Las seis consultas representan **necesidades previstas de acceso** y no son todavía consultas implementadas en MongoDB.
- La frecuencia indicada para cada consulta es una **hipótesis**, no una estadística medida.
- Las reglas del negocio deben distinguirse del mecanismo técnico que posteriormente se utilice para implementarlas.
- El diseño posterior de clientes, equipos y órdenes deberá considerar estas consultas y reglas.
