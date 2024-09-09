import ollama

if not "llama3:8b" in ollama.list().get("models"):                                      # Check for the llama3:8b model locally
    ollama.pull("llama3:8b")                                                            # Pull if it isn't local

print("To exit the chat type 'quit'")                                                   # Inform the user of the loop termination

messages=[]                                                                             # This contains a log of messages from the conversation

while True:
    print()
    message={"role":"user","content":f"{input('Type your message: ')}"}                 # Create a new message
    if message["content"] == "quit": break                                              # Break the loop if the message is 'quit'
    messages.append(message)                                                            # Append message to the log
    stream=ollama.chat(model="llama3:8b",messages=messages,stream=True)                 # Call the Ollama server and return a stream
    ai_response=[]                                                                      # This contains AI Response chunks
    for chunk in stream:                                                                # Iterate through the stream
        content=chunk["message"]["content"]                                             # Get the content from the server response
        ai_response.append(content)                                                     # Append the content to the AI Response
        print(content,end='',flush='')                                                  # Print each chunk in the stream
    messages.append({"role":"assistant","content":"".join(ai_response)})                # Append the AI Response to the message log