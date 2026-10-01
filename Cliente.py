import xmlrpc.client

servidor = xmlrpc.client.ServerProxy(
    "http://localhost:8000/"
)

a = 10
b = 5

resultado = servidor.calcular(a, b)

print("Solicitação enviada ao servidor RPC.")
print(f"Cálculo solicitado: {a} + {b}")
print(f"Resultado recebido: {resultado}")
