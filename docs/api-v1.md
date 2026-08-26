# Atlas Core — API v1

## Objetivo

Definir el primer contrato estable entre Atlas Core, la interfaz web, los módulos y los agentes. La API debe ser versionada (`/api/v1`) y separar claramente operaciones de lectura, diagnóstico y ejecución.

## Convenciones

- Transporte: HTTPS en producción; HTTP solo para desarrollo local controlado.
- Formato: JSON.
- Versionado: `/api/v1`.
- Identificadores: UUID.
- Fechas: ISO 8601 UTC.
- Todas las operaciones administrativas y remotas generan auditoría.
- Los agentes se autentican con identidad propia; no utilizan credenciales de usuarios.

## Recursos iniciales

### Auth

`POST /api/v1/auth/login`

Autentica un usuario y devuelve una sesión/token.

`POST /api/v1/auth/refresh`

Renueva una sesión válida.

`POST /api/v1/auth/logout`

Invalida la sesión.

### Organizations / Sites

`GET /api/v1/organizations`

`POST /api/v1/organizations`

`GET /api/v1/organizations/{id}`

`GET /api/v1/organizations/{id}/sites`

`POST /api/v1/organizations/{id}/sites`

### Devices

`GET /api/v1/devices`

Permite filtrar por organización, sitio, tipo, sistema operativo, estado y agente.

`POST /api/v1/devices`

Registra un dispositivo administrativo cuando corresponda.

`GET /api/v1/devices/{id}`

`GET /api/v1/devices/{id}/health`

`GET /api/v1/devices/{id}/metrics`

### Agents

`POST /api/v1/agents/enroll`

Inicia el registro de un agente mediante un código/token de enrolamiento de un solo uso.

`POST /api/v1/agents/{id}/heartbeat`

Reporta presencia, versión y estado del agente.

`POST /api/v1/agents/{id}/inventory`

Envía inventario estructurado.

`POST /api/v1/agents/{id}/diagnostics`

Envía resultados de pruebas diagnósticas.

`GET /api/v1/agents/{id}/jobs`

Obtiene trabajos autorizados pendientes para el agente.

`POST /api/v1/agents/{id}/jobs/{job_id}/result`

Devuelve el resultado de un trabajo.

### Diagnostics

`POST /api/v1/diagnostics/runs`

Crea una ejecución diagnóstica para un dispositivo.

`GET /api/v1/diagnostics/runs/{id}`

Consulta estado y resultados.

`GET /api/v1/devices/{id}/findings`

Consulta problemas encontrados históricamente.

### Recommendations / Actions

`GET /api/v1/devices/{id}/recommendations`

Obtiene recomendaciones generadas por reglas/IA.

`POST /api/v1/actions/{id}/approve`

Autoriza una acción que requiere aprobación.

`POST /api/v1/actions/{id}/reject`

Rechaza una acción propuesta.

### Jobs

`GET /api/v1/jobs`

`GET /api/v1/jobs/{id}`

`POST /api/v1/jobs/{id}/cancel`

Los trabajos deben conservar estado y trazabilidad completa.

### Audit

`GET /api/v1/audit/events`

Solo usuarios con permiso de auditoría pueden consultar eventos.

## Estados de trabajos

```text
queued
   ↓
running
   ├── succeeded
   ├── failed
   ├── cancelled
   └── awaiting_approval
```

## Modelo de Finding

Un finding debe contener como mínimo:

- `id`
- `device_id`
- `category`
- `severity`
- `title`
- `description`
- `evidence[]`
- `confidence`
- `detected_at`
- `source`
- `status`

`source` identifica si provino de una regla, agente, integración o IA.

## Modelo de Action

Una acción debe contener:

- `id`
- `finding_id`
- `name`
- `description`
- `risk_level`
- `required_permissions[]`
- `requires_approval`
- `parameters_schema`
- `verification_plan`
- `rollback_plan` cuando exista

## Modelo de Agent Job

Un job debe contener:

- `id`
- `agent_id`
- `action_id` o `diagnostic_id`
- `created_at`
- `expires_at`
- `status`
- `parameters`
- `requested_by`
- `approval_id` cuando corresponda
- `result`

## Seguridad

El endpoint de agente no debe permitir un campo genérico como `command: "cualquier comando"`. Las operaciones se modelarán como capacidades explícitas del agente. Ejemplos futuros: `collect_system_inventory`, `collect_event_logs`, `run_network_test`, `repair_dns`, `run_sfc_scan`.

Los parámetros serán validados en servidor antes de ser enviados al agente.

## Compatibilidad

Los agentes deberán declarar versión de protocolo. Atlas Core debe rechazar o degradar de forma segura agentes incompatibles. Las capacidades nuevas deben poder detectarse mediante capability negotiation.
