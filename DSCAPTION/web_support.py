from aiohttp import web

DS_AutoCaptionBot = web.RouteTableDef()

@DS_AutoCaptionBot.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("DS_AutoCaptionBot")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(DS_AutoCaptionBot)
    return web_app
