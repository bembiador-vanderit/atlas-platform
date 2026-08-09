# Atlas Platform — Arquitectura inicial

## Visión
Atlas se plantea como una plataforma SaaS de señalización digital. Un administrador podrá gestionar organizaciones/clientes, ubicaciones, pantallas, contenido multimedia y playlists desde un portal web.

## Componentes

### Portal web
Interfaz administrativa para usuarios autorizados. Gestionará organizaciones, ubicaciones, pantallas, contenido, playlists y publicación.

### API/backend
Responsable de autenticación, autorización, reglas de negocio, persistencia, archivos multimedia, publicación y estado de dispositivos.

### Base de datos
Persistirá usuarios, organizaciones, ubicaciones, dispositivos, medios, playlists, asignaciones y auditoría.

### Almacenamiento multimedia
Vídeos, imágenes y otros recursos deben almacenarse fuera de las tablas SQL. La base de datos conservará metadatos y referencias.

### Player
Aplicación ligera para TV, navegador dedicado o Raspberry Pi. Debe poder registrarse, recibir configuración, descargar contenido, reproducirlo y reportar estado.

## Modelo conceptual
Usuario → Organización → Ubicación → Pantalla/Player.

Contenido → Playlist → Publicación → Pantalla/Player.

La administración de contenido no dependerá de una pantalla concreta; la publicación será una operación explícita.

## Seguridad
- Autenticación centralizada.
- Autorización por organización y rol.
- Credenciales de player independientes de usuarios humanos.
- HTTPS en producción.
- Auditoría de operaciones administrativas.
- No almacenar archivos multimedia grandes directamente en SQL.

## Evolución
El MVP debe permitir posteriormente multiempresa/multicliente, múltiples ubicaciones, grupos de pantallas, programación por horarios, métricas de reproducción y distribución offline.
