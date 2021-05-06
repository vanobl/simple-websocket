from views import socket_list, websocket_handler

def set_routes(app):
    """
        Метод регистрирующий пути приложения.
    """
    app.router.add_get('/', socket_list, name="index")
    app.router.add_get('/ws', websocket_handler, name="ws")