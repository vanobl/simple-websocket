import aiohttp_jinja2
import jinja2
from settings import BASE_DIR
from aiohttp import web
from routes import set_routes
from static import setup_static_routes

# создадим приложение
app = web.Application()

# подключим пути к приложению
set_routes(app)

# подключим путь к статическим файлам
setup_static_routes(app)

# подключим шаблоны
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'templates')))

# запустим приложение
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)