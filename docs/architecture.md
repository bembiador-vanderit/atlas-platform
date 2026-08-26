# Atlas Core — Arquitectura base

## 1. Propósito

Atlas Core será la plataforma común de la familia Atlas. Su responsabilidad será proporcionar identidad, seguridad, auditoría, configuración, APIs, extensibilidad y servicios compartidos para módulos como Atlas Consultorio y Atlas IT.

Atlas Core no debe contener lógica específica de un módulo cuando esta pueda vivir en un módulo independiente.

## 2. Principios

- Modularidad: cada capacidad importante debe poder agregarse o retirarse sin rehacer el núcleo.
- Seguridad por defecto: las acciones destructivas o críticas requieren autorización explícita o una política previamente aprobada.
- Separación de responsabilidades: la IA razona y propone; el motor de políticas decide si una acción puede ejecutarse; los agentes ejecutan y verifican.
- Auditoría completa: toda acción remota debe registrar quién, qué, cuándo, contra qué equipo y con qué resultado.
- Diagnóstico antes de reparación: primero recopilar evidencia, luego determinar causa probable, después proponer/ejecutar una acción y finalmente verificar el resultado.
- Diseño local-first: Atlas IT debe poder operar dentro de una LAN aunque temporalmente no exista Internet.
- Extensible: nuevos diagnósticos, integraciones y acciones deben poder añadirse como módulos/plugins.
- Observabilidad: salud del propio Atlas, agentes, trabajos y errores deben ser visibles.

## 3. Arquitectura lógica

```text
                           ATLAS CORE
                              |
          +-------------------+-------------------+
          |                   |                   |
      Identity            Security            Audit/Event
          |                   |                   |
          +-------------------+-------------------+
                              |
                         Atlas API
                              |
        +---------------------+----------------------+
        |                     |                      |
   Module Registry       Job/Task Engine       Notification
        |                     |                      |
        +---------------------+----------------------+
                              |
                       AI Orchestrator
                              |
                 +------------+-------------+
                 |                          |
          Knowledge Base              Rule Engine
                 |                          |
                 +------------+-------------+
                              |
                       Agent Gateway
                              |
            +----------------+----------------+
            |                |                |
         Windows PC       Windows PC       Server
           Agent            Agent           Agent
```

## 4. Capas

### Atlas Core

Servicios compartidos: usuarios, roles, permisos, organizaciones, equipos, inventario lógico, configuración, auditoría, tareas, notificaciones y registro de módulos.

### Atlas API

Contrato estable entre frontend, módulos, agentes y servicios internos. La API debe versionarse desde el comienzo.

### AI Orchestrator

Coordina el razonamiento de IA. Recibe evidencia estructurada, consulta conocimiento y reglas, genera hipótesis y propuestas de acción. No ejecuta directamente comandos sobre endpoints.

### Rule Engine

Contiene reglas deterministas y políticas de seguridad. Ejemplo: una reparación puede ejecutarse automáticamente si pertenece a la categoría segura y el equipo cumple las condiciones requeridas.

### Job/Task Engine

Convierte diagnósticos y acciones en trabajos trazables. Debe soportar estados como queued, running, succeeded, failed, cancelled y awaiting_approval.

### Agent Gateway

Canal seguro de comunicación con agentes instalados en PCs y servidores. Debe soportar registro, autenticación del agente, heartbeat, envío de diagnósticos, recepción de trabajos y devolución de resultados.

### Agents

Agentes ligeros, inicialmente para Windows, instalados como servicio. No necesitan contener un modelo de IA. Recopilan evidencia, ejecutan herramientas autorizadas y devuelven resultados.

## 5. Flujo de diagnóstico

```text
Síntoma / alerta
      |
      v
Recopilación de evidencia
      |
      v
Normalización
      |
      v
Reglas + conocimiento + IA
      |
      v
Hipótesis / diagnóstico
      |
      v
Plan de reparación
      |
      +----> requiere aprobación ----> usuario/admin
      |
      v
Policy Engine
      |
      v
Agent ejecuta
      |
      v
Verificación posterior
      |
      v
Resultado + auditoría + aprendizaje/caso
```

## 6. Seguridad de agentes

Cada agente tendrá una identidad propia y credenciales rotables. La comunicación deberá usar TLS. El servidor nunca debe aceptar un agente solamente por conocer su IP.

Las acciones remotas deberán utilizar una lista de operaciones permitidas y parámetros validados. No se permitirá ejecutar comandos arbitrarios por defecto.

Los trabajos críticos tendrán aprobación explícita. El sistema deberá registrar la aprobación y el resultado.

## 7. Atlas IT

Atlas IT será el primer módulo que aproveche plenamente el modelo de agentes.

Áreas iniciales:

- Hardware y firmware.
- Windows y componentes del sistema.
- CPU, RAM y almacenamiento.
- SMART y salud de discos.
- Event Viewer y errores recurrentes.
- BSOD y análisis de dumps.
- Servicios y procesos.
- Drivers.
- Rendimiento.
- Red LAN/WAN.
- Wi-Fi.
- DNS, DHCP, gateway y conectividad.
- Pruebas de throughput.
- Seguridad básica y configuración.
- Servidores Windows.
- Hyper-V.
- Docker.
- Impresoras y dispositivos de red.
- Integraciones futuras con UniFi, Omada y MikroTik.

## 8. Modelo de módulos

Cada módulo debe declarar como mínimo:

- identificador y versión;
- capacidades;
- diagnósticos disponibles;
- acciones disponibles;
- requisitos;
- nivel de riesgo;
- permisos requeridos;
- eventos que produce;
- versión mínima de Atlas Core.

## 9. Datos fundamentales

Entidades iniciales previstas:

- User
- Role
- Permission
- Organization
- Site
- Device
- Agent
- AgentCredential
- Module
- DiagnosticRun
- Finding
- Recommendation
- Action
- Job
- Approval
- AuditEvent
- Metric
- Alert
- KnowledgeCase

## 10. Política de IA

La IA debe distinguir entre evidencia, inferencia y acción.

- Evidencia: dato observado por el agente.
- Inferencia: conclusión o hipótesis derivada.
- Acción: operación que modifica el sistema.

Nunca se debe presentar una inferencia como si fuera evidencia. Una acción debe estar vinculada a una razón, riesgo, política y resultado verificable.

## 11. Evolución

La plataforma se construirá por etapas. Primero se estabilizarán Core, API, identidad, auditoría y el agente mínimo. Después se incorporarán diagnósticos y reparaciones de Atlas IT.

La meta de cobertura de aproximadamente 90% será tratada como objetivo de producto y se medirá mediante casos reales, no como una promesa absoluta.
