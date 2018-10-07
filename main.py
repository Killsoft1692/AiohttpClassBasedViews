from aiohttp import web
import json


class IndexView(web.View):
    async def get(self):
        return web.Response(text=json.dumps({'status': 'success', 'method': 'GET'}))

    async def post(self):
        data = self.request.query.get('data', 'EMPTY')
        return web.Response(text=json.dumps({'status': 'success', 'method': 'POST', 'data': data}))

    async def delete(self):
        return web.Response(text=json.dumps({'status': 'success', 'method': 'DELETE'}))


app = web.Application()
app.router.add_view('/', IndexView)
web.run_app(app)
