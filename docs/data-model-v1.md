# Atlas Core — Modelo de datos v1

## Principio

El modelo debe soportar multiempresa, múltiples sitios, dispositivos y agentes sin acoplar Atlas Core a Atlas IT o Atlas Consultorio.

## Entidades

### User

Usuario humano de Atlas.

Campos base: `id`, `email`, `display_name`, `status`, `created_at`, `updated_at`.

### Role

Conjunto reutilizable de permisos.

Campos: `id`, `name`, `description`.

### Permission

Permiso atómico, por ejemplo `devices.read`, `diagnostics.run`, `actions.approve`.

### Organization

Entidad cliente/empresa que agrupa sitios y dispositivos.

Campos: `id`, `name`, `status`, `created_at`.

### Site

Ubicación física o lógica de una organización.

Campos: `id`, `organization_id`, `name`, `address`, `timezone`, `status`.

### Device

Equipo administrado por Atlas.

Campos previstos: `id`, `site_id`, `hostname`, `device_type`, `os_family`, `os_version`, `serial_number`, `status`, `last_seen_at`, `created_at`, `updated_at`.

`device_type` podrá incluir `workstation`, `server`, `network_device`, `printer`, `nas`, etc.

### Agent

Instancia de software instalada en un dispositivo.

Campos: `id`, `device_id`, `agent_version`, `protocol_version`, `status`, `last_heartbeat_at`, `capabilities`, `installed_at`, `updated_at`.

### AgentCredential

Identidad técnica del agente. Nunca se almacena el secreto en texto plano.

Campos: `id`, `agent_id`, `credential_type`, `issued_at`, `expires_at`, `revoked_at`, `last_used_at`.

### Module

Módulo Atlas instalado/registrado.

Campos: `id`, `module_id`, `version`, `status`, `capabilities`, `minimum_core_version`.

### DiagnosticRun

Ejecución de un conjunto de diagnósticos sobre un dispositivo.

Campos: `id`, `device_id`, `requested_by`, `profile`, `status`, `started_at`, `finished_at`.

### Finding

Problema o anomalía detectada.

Campos: `id`, `diagnostic_run_id`, `device_id`, `category`, `severity`, `title`, `description`, `confidence`, `source`, `status`, `detected_at`.

### Evidence

Dato observado que respalda un finding. Puede ser métrica, evento, comando estructurado, inventario o resultado de prueba.

Campos: `id`, `finding_id`, `type`, `name`, `value`, `unit`, `observed_at`, `source`.

### Recommendation

Propuesta de resolución asociada a uno o más findings.

Campos: `id`, `finding_id`, `title`, `description`, `risk_level`, `confidence`, `created_at`.

### Action

Operación ejecutable por un agente o servicio autorizado.

Campos: `id`, `recommendation_id`, `action_type`, `parameters_schema`, `risk_level`, `requires_approval`, `verification_plan`, `rollback_plan`, `status`.

### Approval

Autorización humana o por política para una acción.

Campos: `id`, `action_id`, `requested_by`, `approved_by`, `status`, `reason`, `created_at`, `expires_at`.

### Job

Trabajo entregado a un agente.

Campos: `id`, `agent_id`, `action_id`, `status`, `parameters`, `created_at`, `started_at`, `finished_at`, `expires_at`, `result`.

### Metric

Medición temporal de rendimiento o salud.

Campos: `id`, `device_id`, `metric_type`, `value`, `unit`, `captured_at`, `source`.

### Alert

Evento que requiere atención.

Campos: `id`, `device_id`, `severity`, `type`, `title`, `description`, `status`, `created_at`, `resolved_at`.

### AuditEvent

Registro inmutable de acciones y eventos relevantes.

Campos: `id`, `actor_type`, `actor_id`, `organization_id`, `device_id`, `event_type`, `action`, `metadata`, `created_at`.

### KnowledgeCase

Caso técnico reutilizable para enriquecer diagnósticos futuros.

Campos: `id`, `module_id`, `problem_signature`, `symptoms`, `evidence`, `diagnosis`, `actions`, `verification`, `outcome`, `confidence`, `created_at`.

## Relaciones principales

```text
Organization 1 ─── N Site
Site         1 ─── N Device
Device       1 ─── N Agent
Device       1 ─── N DiagnosticRun
DiagnosticRun 1 ─ N Finding
Finding      1 ─── N Evidence
Finding      1 ─── N Recommendation
Recommendation 1 ─ N Action
Action       1 ─── N Approval
Action       1 ─── N Job
Device       1 ─── N Metric
Device       1 ─── N Alert
```

## Retención

Los datos operativos y métricas tendrán políticas de retención configurables. Los eventos de auditoría y casos de conocimiento tendrán una retención superior y no deberán eliminarse como parte de una limpieza rutinaria.

## Multi-tenant

Todas las consultas de recursos pertenecientes a una organización deben aplicar autorización por tenant. Un usuario no debe poder acceder a dispositivos de otra organización solamente conociendo su UUID.
