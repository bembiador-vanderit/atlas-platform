# Atlas Core — Roadmap inicial

## Fase 0 — Fundación

- [x] Crear repositorio Atlas Platform.
- [x] Definir arquitectura lógica.
- [x] Definir separación Core / módulos / agentes / IA.
- [x] Definir principios de seguridad.
- [ ] Definir contrato API v1.
- [ ] Definir modelo de datos inicial.
- [ ] Definir sistema de módulos/plugins.

## Fase 1 — Atlas Core mínimo

- [ ] Backend API.
- [ ] PostgreSQL.
- [ ] Autenticación.
- [ ] Usuarios, roles y permisos.
- [ ] Auditoría.
- [ ] Registro de dispositivos.
- [ ] Registro de agentes.
- [ ] Job engine básico.
- [ ] Health checks.
- [ ] Docker Compose para desarrollo.

## Fase 2 — Atlas IT Agent

- [ ] Agente Windows como servicio.
- [ ] Registro seguro del agente.
- [ ] Heartbeat.
- [ ] Inventario de hardware.
- [ ] Inventario de software.
- [ ] CPU/RAM/disco.
- [ ] Red básica.
- [ ] Event Viewer.
- [ ] Métricas básicas.
- [ ] Ejecución de tareas seguras.
- [ ] Verificación posterior.

## Fase 3 — Diagnóstico inteligente

- [ ] Motor de reglas.
- [ ] Findings normalizados.
- [ ] Base de conocimiento.
- [ ] Orquestador de IA.
- [ ] Explicación de causa probable.
- [ ] Recomendaciones.
- [ ] Priorización por riesgo.
- [ ] Historial por dispositivo.

## Fase 4 — Reparación

- [ ] Catálogo de acciones seguras.
- [ ] Aprobaciones.
- [ ] Dry-run cuando sea posible.
- [ ] Rollback cuando sea posible.
- [ ] Verificación automática.
- [ ] Registro completo de resultados.

## Fase 5 — Red

- [ ] Ping y pérdida de paquetes.
- [ ] Latencia gateway/LAN/Internet.
- [ ] DNS.
- [ ] DHCP.
- [ ] Traceroute.
- [ ] Velocidad de enlace.
- [ ] Throughput LAN.
- [ ] Throughput Internet.
- [ ] Wi-Fi.
- [ ] Detección de anomalías.

## Fase 6 — Servidores

- [ ] Windows Server.
- [ ] Active Directory.
- [ ] DNS/DHCP.
- [ ] RDP.
- [ ] Hyper-V.
- [ ] Docker.
- [ ] Análisis de BSOD.
- [ ] MEMORY.DMP / WinDbg.
- [ ] RAID/almacenamiento.

## Fase 7 — Ecosistema Atlas

- [ ] Integración Atlas Consultorio.
- [ ] Integraciones UniFi.
- [ ] Integraciones Omada.
- [ ] Integraciones MikroTik.
- [ ] Impresoras.
- [ ] NAS.
- [ ] Notificaciones.
- [ ] Reportes técnicos.
- [ ] Panel multiempresa.

## Regla de evolución

Cada problema nuevo encontrado en producción podrá convertirse en una nueva regla, diagnóstico, acción, integración o módulo. Antes de incorporarlo al catálogo automático debe documentarse, probarse y clasificarse por riesgo.
