from spyne import Application, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import asyncio
from aiohttp import ClientSession

async def getOpenWeatherMapInfo(latitud, longitud):
    async with ClientSession() as session:
        appId = '9cb52920753b6d5a99a013c8006848b9'
        apiUrl = f'https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={appId}'
        async with session.get(apiUrl) as response:
            response = await response.read()
            print(response)

class Clima(ServiceBase):

    @rpc(float, float, _returns= {}) 
    def temperatura(ctx, latitud: float, longitud: float) -> {}:
        return a+b
    
    @rpc(float, float, _returns= {})
    def viento(ctx, latitud: float, longitud: float) -> {}:
        return a-b

    @rpc(float, float, _returns= float)
    def humedad(ctx, latitud: float, longitud: float) -> float:
        return a*b

    @rpc(float, float, _returns= float)
    def presion(ctx,  latitud: float, longitud: float) -> float:
        return latitud

    @rpc(float, float, _returns= float)
    def visibilidad(ctx, latitud:float, longitud:float) -> float:
        return latitud

application = Application(
    services=[Clima],
    tns='http://tests.python-zeep.org/',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11())

application = WsgiApplication(application)

if __name__ == '__main__':
    '''
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, application)
    server.serve_forever()
    '''
    asyncio.get_event_loop().run_until_complete(getOpenWeatherMapInfo(10.25,20.1))
    