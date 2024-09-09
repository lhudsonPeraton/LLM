from discord import Intents, Interaction, Message # type: ignore
from discord.ext.commands import Bot # type: ignore
from configparser import ConfigParser
from ollama import pull, list, chat
from logging import FileHandler

config = ConfigParser()
config.read('config.ini')
token=config["Discord"]["token"]
channel=config["Discord"]["channel"]
model=config["Ollama"]["model"]
intents=Intents.default()
intents.message_content = True
bot=Bot(command_prefix="/",intents=intents)
log_handler=FileHandler(filename="discord.log",encoding="utf-8",mode="w")

@bot.tree.command(name="cbt", description="Replies to a message using the AI model")
async def cbt(interaction:Interaction, message:str):
    if interaction.channel.id != int(channel):
        await interaction.response.send_message("Why don't you meet me in the bot-channel :stuck_out_tongue_winking_eye:", ephemeral=True)
        return
    messages=[]
    async for msg in interaction.channel.history(limit=20):
        messages.append({"role": "user" if msg.author != bot.user else "assistant", "content": msg.content})
    messages.reverse()
    # print(messages)
    messages.append({"role": "user", "content": message})
    await interaction.response.defer()
    try:
        async with interaction.channel.typing():
            if model not in list().get("models"):
                pull(model)
            response = chat(model=model, messages=messages, options={"num_predict": 1000})
    except Exception as e:
        response = {"message": {"content": "Error"}}
    await interaction.followup.send(response.get("message", {}).get("content", "Error"))

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

bot.run(token, log_handler=log_handler)