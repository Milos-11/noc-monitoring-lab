import socket

host = "8.8.8.8"
port = 53

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

resultado = sock.connect_ex((host, port))

if resultado == 0:
    print(f"[OK] {host}:{port} está abierto")
else:
    print(f"[ALERTA] {host}:{port} no está disponible")

sock.close() 
