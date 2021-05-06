def setup_static_routes(app):
    """
        Метод-указатель на статические файлы.
    """
    app.router.add_static('/static/', path='static', name='static')