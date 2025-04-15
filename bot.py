from botbuilder.core import TurnContext, ActivityHandler
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class LLMTeamsBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if available
            messages=[{"role": "user", "content": user_input}],
        )
        await turn_context.send_activity(response.choices[0].message["content"])
