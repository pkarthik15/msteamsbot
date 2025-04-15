from botbuilder.core import BotFrameworkAdapterSettings, BotFrameworkAdapter
from botbuilder.core.integration import aiohttp_bot_framework_http_adapter
from dotenv import load_dotenv
import os


load_dotenv()


settings = BotFrameworkAdapterSettings(os.getenv("APP_ID"), os.getenv("APP_PASSWORD"))
adapter = BotFrameworkAdapter(settings)
