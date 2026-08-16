# NOC Monitoring Lab

Laboratorio práctico de monitorización de sistemas y redes desarrollado con Python y Linux.

El proyecto simula tareas básicas de un entorno NOC (Network Operations Center), realizando comprobaciones de disponibilidad de hosts y servicios, generando alertas y registrando los resultados en archivos de log.

## Objetivos

Este laboratorio tiene como objetivos:

- Comprobar la disponibilidad de hosts mediante `ping`.
- Monitorizar diferentes hosts de forma automatizada.
- Comprobar la disponibilidad de servicios mediante puertos TCP.
- Generar estados de monitorización `OK` y `CRITICAL`.
- Registrar eventos con fecha y hora.
- Practicar automatización de tareas de monitorización con Python.
- Utilizar Git y GitHub para control de versiones y documentación del proyecto.

## Tecnologías utilizadas

- Python 3
- Linux / Ubuntu
- Git
- GitHub
- Bash
- `subprocess`
- `socket`
- ICMP / `ping`
- TCP
- Logging

## Estructura del proyecto

```text
noc-monitoring-lab/
│
├── .gitignore
├── README.md
├── monitor.py
├── monitor_with_log.py
├── port_monitor.py
│
└── logs/
    └── monitoring.log


Scripts
monitor.py

Realiza una comprobación básica de disponibilidad de varios hosts mediante ping.

Actualmente monitoriza:

8.8.8.8
1.1.1.1
192.0.2.1

Ejemplo de salida:

[OK] 8.8.8.8 responde
[OK] 1.1.1.1 responde
[ALERTA] 192.0.2.1 no responde

La dirección 192.0.2.1 se utiliza como destino de prueba para simular una incidencia de disponibilidad.

port_monitor.py

Comprueba la disponibilidad de un servicio TCP mediante una conexión socket.

Ejemplo:

[OK] 8.8.8.8:53 está abierto

El puerto 53 se utiliza como ejemplo de servicio DNS.

monitor_with_log.py

Amplía la monitorización de hosts incorporando:

Fecha y hora del evento.
Estado de monitorización.
Registro persistente en un archivo de log.
Estados OK y CRITICAL.

Ejemplo:

2026-08-14 17:29:35 | 8.8.8.8 | OK
2026-08-14 17:29:35 | 1.1.1.1 | OK
2026-08-14 17:29:45 | 192.0.2.1 | CRITICAL
Ejecución
Monitorización básica
python3 monitor.py
Monitorización de puertos
python3 port_monitor.py
Monitorización con registro de eventos
python3 monitor_with_log.py

El archivo de log se genera en:

logs/monitoring.log
Conceptos de NOC practicados

Este laboratorio permite practicar conceptos básicos relacionados con:

Host availability monitoring
Service availability monitoring
Network connectivity
TCP port monitoring
Event logging
Alert classification
Incident detection
Automation
Troubleshooting
Control de versiones

El proyecto utiliza Git para el control de versiones.

Primer commit:

9539c21 - Initial NOC monitoring lab

Repositorio:

GitHub: https://github.com/Milos-11/noc-monitoring-lab

Próximas mejoras

El laboratorio continuará evolucionando con nuevas funcionalidades:

 Detección de cambios de estado.
 Registro de eventos de recuperación.
 Monitorización periódica automática.
 Mejora de niveles de severidad.
 Monitorización de múltiples puertos.
 Análisis de logs.
 Generación de estadísticas.
 Sistema de alertas.
 Integración de conceptos de IA para asistencia en el análisis de incidencias.
Objetivo profesional

Este proyecto forma parte de un portfolio práctico orientado al desarrollo de competencias para puestos de:

NOC Operator
Técnico de Monitorización
Operador de Sistemas
Técnico de Sistemas Junior
Network Monitoring
IT Operations

El objetivo es demostrar mediante proyectos prácticos conocimientos de Linux, Python, redes, monitorización, troubleshooting, automatización y Git/GitHub.
