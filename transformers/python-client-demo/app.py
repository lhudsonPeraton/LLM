import torch
from transformers import pipeline
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

HF_TOKEN=config["Huggingface"]["token"]

pipe = pipeline(
    "text-generation", 
    "meta-llama/Meta-Llama-3-8B-Instruct", 
    torch_dtype=torch.bfloat16, 
    device_map="auto",
    token=HF_TOKEN)

print("To exit the chat type 'quit'")

messages=[]

while True:
    print()
    message={"role":"user","content":f"{input('Type your message: ')}"}
    if message["content"] == "quit": break
    messages.append(message)
    response=pipe(messages)
    content=response[0]['generated_text'][-1]['content']
    print(content)
    messages.append({"role":"assistant","content":content})