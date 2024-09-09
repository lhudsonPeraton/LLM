# hackathon-demos

## Prerequisite

- [ ] Install Docker
- [ ] Install Python

## Setup Python Virtual Environment
- [ ] py -m venv venv
- [ ] source venv/Scripts/activate 

## Ollama

- [ ] pip install -r ollama/requirements.txt
- [ ] docker run -p 11434:11434 ollama/ollama -this takes long cause its pulling shit
    - To mount to save runtime add -v <anywhere on host>:/root/.ollama/models
    - Models will persist if you specify the same place everytime you run the container
- [ ] pip install -r requirements.txt
- [ ] pip install tensorflow
- [ ] pip install accelerate 

## Huggingface transformer

- [ ] Make huggingface account request access for API key, will take a few minutes

- [ ] Run it, it will take a few minutes
    - Transformers takes longer


## Discord Bot

- [ ] [Look up how to make a discord bot](https://discordpy.readthedocs.io/en/stable/discord.html)
- [ ] Run the ollama container 

### Discord Bot Token Tips

- [ ] Reset bot token after creating it 
- [ ] Give the bot Meesage Content Intent permission (just a tick box)
- [ ] Generate a new oauth2 token with scope - bot and permissions - send and read messages