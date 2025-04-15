from botbuilder.core import BotFrameworkAdapterSettings, BotFrameworkAdapter
from dotenv import load_dotenv
import os


load_dotenv()


settings = BotFrameworkAdapterSettings(os.getenv("APP_ID"), os.getenv("APP_PASSWORD"))
adapter = BotFrameworkAdapter(settings)
