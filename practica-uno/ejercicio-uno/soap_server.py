from spyne import Application, rpc, ServiceBase, Integer
from spyne import server

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, a, b):
        return a - b

    @rpc(Integer, Integer, _returns=Integer)
    def multiply(ctx, a, b):
        return a * b

    @rpc(Integer, Integer, _returns=Integer)
    def divide(ctx, a, b):
        if b == 0:
            raise ValueError("División por cero no está permitida.")
        return a // b

application = Application([CalculatorService], 'calculator.soap',
                          in_protocol=server.soap11(validator='lxml'),
                          out_protocol=server.soap11(),
                          ignore_preferred_marshaler_option=True)

if __name__ == '__main__':
    from spyne import wsgi_app
    wsgi_app = wsgi_app.WsgiApplication(application)
    server = wsgi_app.make_server('localhost', 8000)
    print("Servidor SOAP escuchando en http://localhost:8000")
    server.serve_forever()
