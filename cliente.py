from zeep import Client

client = Client('http://localhost:8000/?wsdl')

result = client.service.temperatura(10.5, 11.5)
print(result)
result = client.service.viento(10.5, 11.5)
print(result)
result = client.service.humedad(10.5, 11.5)
print(result)
result = client.service.presion(10.5, 11.5)
print(result)
result = client.service.visibilidad(10.5, 11.5)
print(result)