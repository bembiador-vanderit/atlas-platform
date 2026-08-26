# Atlas Core — Estructura de proyecto v1

```text
atlas-platform/
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── api-v1.md
│   ├── data-model-v1.md
│   └── project-structure-v1.md
│
├── core/
│   ├── api/
│   ├── auth/
│   ├── organizations/
│   ├── devices/
│   ├── agents/
│   ├── jobs/
│   ├── diagnostics/
│   ├── audit/
│   └── modules/
│
├── atlas-it/
│   ├── diagnostics/
│   ├── actions/
│   ├── rules/
│   └── integrations/
│
├── agent-windows/
│   ├── agent/
│   ├── collectors/
│   ├── capabilities/
│   ├── transport/
│   └── installer/
│
├── ai/
│   ├── orchestrator/
│   ├── prompts/
│   ├── knowledge/
│   └── policies/
│
├── web/
│   ├── dashboard/
│   ├── devices/
│   ├── diagnostics/
│   ├── jobs/
│   └── settings/
│
├── infrastructure/
│   ├── docker/
│   ├── database/
│   └── deployment/
│
└── tests/
    ├── core/
    ├── atlas-it/
    ├── agent/
    └── integration/
```

## Regla de dependencia

- `core` no depende de `atlas-it`.
- `atlas-it` depende de contratos de `core`.
- `agent-windows` implementa el contrato de agente; no contiene lógica de negocio del Core.
- `ai` consume evidencia y contratos, pero no obtiene acceso directo a sistemas operativos.
- `web` consume la API y no debe ejecutar acciones administrativas directamente.

## Primera implementación

La primera entrega de código será deliberadamente pequeña:

1. API FastAPI.
2. PostgreSQL.
3. migraciones.
4. health endpoint.
5. estructura de configuración.
6. modelos base Organization/Site/Device/Agent.
7. Docker Compose de desarrollo.
8. pruebas de API.

Después se agregará autenticación y, finalmente, el agente Windows.
