import aiohttp_jinja2
import json
from aiohttp import web, WSMsgType


@aiohttp_jinja2.template('socket_list.html')
async def socket_list(request):
    """
        Метод отображения формы и списка вопросов.
    """

    return {'title': 'Список вопросов'}


async def websocket_handler(request):
    """
        Метод обработки запросов websocket.
        На вход принимает строку, содержащую JSON.
        Парсит её. И отдаёт в ответ JSON, который\n
        на стороне клиента считывается.
    """
    clients = {}
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    clients[ws] = 0

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            json_object = json.loads(msg.data)
            
            if json_object['text'] == 'close':
                await ws.close()
            else:
                json_object['text'] = f'{json_object["text"]}'
                clients[ws] += 1
                json_object['last_number'] = clients[ws]
                await ws.send_json(json_object)
                
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'ws соединение закрыто с ошибкой {ws.exception()}')

    del clients[ws]

    return ws