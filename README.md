# NOC Monitoring Lab

Laboratorio práctico de monitorización de sistemas, redes y servicios desarrollado con Python y Linux.

El proyecto simula algunas tareas básicas de un entorno NOC (Network Operations Center), incluyendo comprobación de disponibilidad de hosts, monitorización de servicios TCP, persistencia de estados y detección de incidentes y recuperaciones.

## Objetivos

- Monitorizar la disponibilidad de diferentes hosts mediante ICMP/ping.
- Comprobar la disponibilidad de servicios mediante conexiones TCP.
- Mantener el estado conocido de cada elemento monitorizado.
- Detectar cambios entre estados.
- Identificar nuevos incidentes.
- Detectar recuperaciones de servicios.
- Registrar los resultados de las comprobaciones.
- Utilizar Git y GitHub siguiendo un flujo de trabajo basado en ramas y Pull Requests.

## Tecnologías utilizadas

- Python 3
- Linux / Ubuntu
- Git
- GitHub
- TCP/IP
- ICMP
- JSON
- Sockets Python
- Bash

## Funcionalidades

### 1. Monitorización de hosts

El laboratorio comprueba la disponibilidad de:

- `8.8.8.8`
- `1.1.1.1`
- `192.0.2.1`

Ejemplo:

```text
[OK] 8.8.8.8 responde
[OK] 1.1.1.1 responde
[ALERTA] 192.0.2.1 no responde

Monitorización de servicios TCP

También se puede comprobar la disponibilidad de un servicio TCP:

127.0.0.1:8080

Para realizar la prueba se utilizó un servidor HTTP de Python:

python3 -m http.server 8080

La conectividad del puerto se comprobó mediante:

nc -zv 127.0.0.1 8080
Detección de estados

El monitor mantiene el último estado conocido de cada host o servicio mediante un archivo JSON.

Ejemplo:

{
    "8.8.8.8": "OK",
    "1.1.1.1": "OK",
    "192.0.2.1": "CRITICAL",
    "127.0.0.1:8080": "CRITICAL"
}

Esto permite comparar el estado anterior con el estado actual.

Estados
OK
CRITICAL

Cuando el estado permanece igual:

[SIN CAMBIO] 127.0.0.1:8080: OK

Cuando un servicio deja de estar disponible:

[INCIDENTE] 127.0.0.1:8080: OK -> CRITICAL

Cuando el servicio vuelve a estar disponible:

[RECOVERY] 127.0.0.1:8080: CRITICAL -> OK
Flujo de monitorización
             Monitorización
                    |
          +---------+---------+
          |                   |
        Hosts              Servicios
          |                   |
        ICMP                 TCP
          |                   |
          +---------+---------+
                    |
             Estado actual
                    |
             Comparación
                    |
          +---------+---------+
          |         |         |
      SIN CAMBIO INCIDENTE RECOVERY
Scripts
monitor.py

Realiza una comprobación básica de disponibilidad de hosts mediante ping.

monitor_with_log.py

Versión avanzada del monitor que incorpora:

persistencia de estados;
registro de resultados;
detección de cambios de estado;
detección de incidentes;
detección de recuperaciones;
monitorización de servicios TCP.
port_monitor.py

Comprueba la disponibilidad de un puerto TCP concreto mediante sockets.

Estructura del proyecto
noc-monitoring-lab/
│
├── .gitignore
├── README.md
├── monitor.py
├── monitor_with_log.py
├── port_monitor.py
│
└── logs/
    ├── monitoring.log
    └── status.json

La carpeta logs/ contiene archivos generados durante la ejecución y está excluida del repositorio mediante .gitignore.

Ejecución

Clonar el repositorio:

git clone https://github.com/Milos-11/noc-monitoring-lab.git

Entrar en el directorio:

cd noc-monitoring-lab

Ejecutar el monitor básico:

python3 monitor.py

Ejecutar el monitor avanzado:

python3 monitor_with_log.py

Comprobar un puerto TCP:

python3 port_monitor.py
Prueba de incidente y recuperación

Para probar la monitorización de servicios se utilizó un servidor HTTP local:

python3 -m http.server 8080

Con el servicio activo:

127.0.0.1:8080 -> OK

Al detener el servidor:

OK -> CRITICAL

El monitor genera:

[INCIDENTE] 127.0.0.1:8080: OK -> CRITICAL

Al volver a iniciar el servidor:

CRITICAL -> OK

El monitor genera:

[RECOVERY] 127.0.0.1:8080: CRITICAL -> OK
Registro de eventos

Los resultados se almacenan en:

logs/monitoring.log

Ejemplo:

2026-08-14 17:22:39 | 8.8.8.8 | OK
2026-08-14 17:22:39 | 1.1.1.1 | OK
2026-08-14 17:22:49 | 192.0.2.1 | ALERTA

El estado actual se mantiene en:

logs/status.json

Estos archivos son generados durante la ejecución y no se incluyen en GitHub.

Control de versiones

El proyecto utiliza Git siguiendo un flujo basado en ramas:

main
 |
 +-- feature/state-change-detection
             |
             +-- desarrollo
             |
             +-- pruebas
             |
             +-- commit
             |
             +-- Pull Request
             |
             +-- merge
             |
             v
           main
Competencias demostradas

Este laboratorio permite demostrar conocimientos prácticos relacionados con:

Network Monitoring
Service Monitoring
TCP/IP
ICMP
Python scripting
Linux
Troubleshooting
State persistence
Incident detection
Recovery detection
Log management
Git
GitHub
Pull Requests
Branching
Control de versiones
Próximas mejoras

Posibles ampliaciones del laboratorio:

monitorización periódica automática;
configuración de hosts desde un archivo externo;
monitorización de múltiples puertos;
niveles de severidad;
generación de métricas;
alertas por correo electrónico;
integración con una API;
dashboard de monitorización;
Dockerización del laboratorio;
integración con herramientas de monitorización como Prometheus o Grafana.
