import subprocess

hosts = [
    "8.8.8.8",
    "1.1.1.1",
    "192.0.2.1"
]

for host in hosts:

    resultado = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if resultado.returncode == 0:
        print(f"[OK] {host} responde")
    else:
        print(f"[ALERTA] {host} no responde")
