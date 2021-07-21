from zeep import Client

client = Client('http://localhost:8000/?wsdl')

result = client.service.suma(4,5)

print(result)