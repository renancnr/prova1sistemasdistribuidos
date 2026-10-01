from xmlrpc.server import SimpleXMLRPCServer


def calcular(a, b):
    resultado = a + b
    return resultado


servidor = SimpleXMLRPCServer(
    ("localhost", 8000),
    allow_none=True
)

servidor.register_function(calcular, "calcular")

print("Servidor RPC iniciado.")
print("Aguardando solicitações...")

servidor.serve_forever()
