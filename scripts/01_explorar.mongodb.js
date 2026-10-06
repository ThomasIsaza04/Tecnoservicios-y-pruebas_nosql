// =============================================================================
// Actividad A4: Laboratorio Inicial de MongoDB - TecnoServicios
// File: scripts/01_explorar.js
// =============================================================================

// Usar o crear la base de datos de trabajo
use('tecnoservicios_db');

// Limpiar la colección de demostración si ya existe
db.ordenes_demo.drop();

// 1. Inserción de la orden OS-DEMO-001 (Portátil con tipo Date nativo)
db.ordenes_demo.insertOne({
  numero_orden: "OS-DEMO-001",
  cliente: {
    alias: "cliente_ana"
  },
  equipo: {
    codigo: "EQ-101",
    tipo: "portatil",
    especificaciones: {
      ram_gb: 16,
      almacenamiento: "512GB SSD"
    }
  },
  estado: "recibida",
  prioridad: "alta",
  fecha_ingreso: ISODate("2026-10-06T08:00:00Z"),
  fecha_compromiso: ISODate("2026-10-10T18:00:00Z")
});

// 2. Transferencia: Inserción de la orden OS-DEMO-002 (Teléfono móvil)
db.ordenes_demo.insertOne({
  numero_orden: "OS-DEMO-002",
  cliente: {
    alias: "cliente_luis"
  },
  equipo: {
    codigo: "EQ-102",
    tipo: "telefono",
    especificaciones: {
      bateria_salud_porcentaje: 88,
      pantalla_pulgadas: 6.1
    }
  },
  estado: "en_diagnostico",
  prioridad: "media",
  fecha_ingreso: ISODate("2026-10-06T09:30:00Z"),
  fecha_compromiso: ISODate("2026-10-08T17:00:00Z")
});

// 3. Consultas de Verificación
print("\n--- 1. Listado de todos los documentos insertados ---");
console.log(db.ordenes_demo.find().toArray());

print("\n--- 2. Validación de tipos de datos de fecha en OS-DEMO-001 ---");
let doc = db.ordenes_demo.findOne({ numero_orden: "OS-DEMO-001" });

// Comprobación de tipo Date nativo de JS/BSON
let esFecha = doc.fecha_ingreso instanceof Date || Object.prototype.toString.call(doc.fecha_ingreso) === '[object Date]';
print("Tipo de fecha_ingreso: " + (esFecha ? "Date (Correcto)" : "String/Otro"));