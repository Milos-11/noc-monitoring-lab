import subprocess
from datetime import datetime

hosts = [
    "8.8.8.8",
    "1.1.1.1",
    "192.0.2.1"
]

log_file = "logs/monitoring.log"

for host in hosts:

    resultado = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if resultado.returncode == 0:
        estado = "OK"
        print(f"[OK] {host} responde")

    else:
        estado = "CRITICAL"
        print(f"[CRITICAL] {host} no responde")

    with open(log_file, "a") as archivo:
        archivo.write(f"{fecha} | {host} | {estado}\n")
