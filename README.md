# Atlas Platform

Atlas es una plataforma modular para diagnóstico, administración y automatización técnica.

## Componentes

- **Atlas Core** — identidad, seguridad, dispositivos, agentes, tareas, auditoría y APIs compartidas.
- **Atlas IT** — diagnóstico, reparación, optimización y monitoreo de PCs, servidores y redes.
- **Atlas Agent** — agente ligero para endpoints, inicialmente Windows.
- **Atlas AI** — orquestación de IA, conocimiento y razonamiento técnico.
- **Atlas Web** — consola central de administración.

## Principio

Atlas debe observar, diagnosticar, proponer, ejecutar de forma controlada y verificar el resultado. Las acciones de alto riesgo requieren autorización y toda acción remota queda auditada.

## Estado

Proyecto en fase de fundación. La especificación técnica se encuentra en `docs/`.

## Próximo hito

Construir el Core mínimo ejecutable con FastAPI, PostgreSQL, migraciones, configuración, health check, modelos iniciales y pruebas.
