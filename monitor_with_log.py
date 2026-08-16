import subprocess
import json
import socket
from datetime import datetime

hosts = [
    "8.8.8.8",
    "1.1.1.1",
    "192.0.2.1"
]

services = [
    ("127.0.0.1", 8080)
]

log_file = "logs/monitoring.log"
status_file = "logs/status.json"


# Cargar estados anteriores
try:
    with open(status_file, "r") as archivo:
        estados_anteriores = json.load(archivo)
except FileNotFoundError:
    estados_anteriores = {}


estados_actuales = {}


def registrar_estado(nombre, estado):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    estados_actuales[nombre] = estado

    estado_anterior = estados_anteriores.get(nombre)

    if estado_anterior is None:
        print(f"[INFO] {nombre} estado inicial: {estado}")

    elif estado_anterior != estado:

        if estado == "CRITICAL":
            print(
                f"[INCIDENTE] {nombre}: "
                f"{estado_anterior} -> {estado}"
            )

        elif estado == "OK":
            print(
                f"[RECOVERY] {nombre}: "
                f"{estado_anterior} -> {estado}"
            )

    else:
        print(f"[SIN CAMBIO] {nombre}: {estado}")

    with open(log_file, "a") as archivo:
        archivo.write(
            f"{fecha} | {nombre} | {estado}\n"
        )


# Monitorización de hosts
for host in hosts:

    resultado = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if resultado.returncode == 0:
        estado = "OK"
    else:
        estado = "CRITICAL"

    registrar_estado(host, estado)


# Monitorización de servicios TCP
for host, port in services:

    nombre = f"{host}:{port}"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    resultado = sock.connect_ex((host, port))

    if resultado == 0:
        estado = "OK"
    else:
        estado = "CRITICAL"

    sock.close()

    registrar_estado(nombre, estado)


# Guardar estados actuales
with open(status_file, "w") as archivo:
    json.dump(estados_actuales, archivo, indent=4)
