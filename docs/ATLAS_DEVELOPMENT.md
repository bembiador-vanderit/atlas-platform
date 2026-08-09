# Atlas Platform — Guía de desarrollo

## Objetivo
Atlas será una plataforma central para administrar contenido y reproducción en pantallas digitales, comenzando por el MVP para clientes con múltiples negocios y pantallas.

## Principios
- Arquitectura modular y preparada para crecer.
- Separación clara entre portal web, backend/API, base de datos, almacenamiento y player.
- Seguridad, autenticación, permisos y trazabilidad desde el inicio.
- Independencia respecto a una marca concreta de TV o dispositivo.
- Cambios pequeños, comprobables y documentados.

## Primera etapa
1. Definir arquitectura base.
2. Crear backend y modelo de datos inicial.
3. Crear autenticación y organizaciones/clientes.
4. Gestionar ubicaciones y pantallas/dispositivos.
5. Gestionar biblioteca multimedia y playlists.
6. Publicar contenido hacia pantallas.
7. Preparar cliente reproductor para TV/Raspberry Pi.
8. Añadir monitoreo, logs y estado de dispositivos.

## Criterio de MVP
Primero debe existir una base funcional para usuarios, organizaciones, pantallas, contenido y playlists. Las funciones avanzadas —programación, métricas, grupos y distribución offline— se incorporarán después sobre esa base.
