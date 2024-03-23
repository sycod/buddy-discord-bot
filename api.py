"""FastAPI server for chatbot AI"""

from models.buddy import ask_buddy

import discord
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def send_message(message, user_message, is_private):
    """Send a message to the user or channel"""
    try:
        response = ask_buddy(user_message)
        answer = response["choices"][0]["message"]["content"]
        if is_private:
            await message.author.send(answer)
        else:
            await message.channel.send(answer)

        print(f'Usage: {response["usage"]}')

    except Exception as e:
        print(e)


def run_bot():
    """Run the Discord client server and manage events"""
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} est vivant !")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} in {channel} sent: {user_message}")

        if message.channel.type == discord.ChannelType.private:
            await send_message(message, user_message, True)
        elif user_message[0] == "@Buddy ":
            user_message = user_message[6:]
            await send_message(message, user_message, True)
        elif "<@1219776032719241357>" in user_message:
            await send_message(message, user_message, False)
        else:
            pass

    client.run(TOKEN)


if __name__ == "__main__":
    run_bot()
