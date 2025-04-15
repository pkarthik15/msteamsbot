import os
from aiohttp import web
from adapters import adapter
from bot import LLMTeamsBot

bot = LLMTeamsBot()

async def messages(req: web.Request) -> web.Response:
    body = await req.json()
    print(body)
    auth_header = req.headers.get("Authorization", "")
    response = await adapter.process_activity(body, auth_header, bot.on_turn)
    return web.Response(status=response.status)

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=3978)
