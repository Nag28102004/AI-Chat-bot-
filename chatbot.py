import ollama #type:ignore
import json
import os 
import subprocess
import sys


# Open a new Windows Terminal
if os.environ.get("CHATBOT_NEW_TERM") != "1":

    script = os.path.abspath(__file__)

    env = os.environ.copy()
    env["CHATBOT_NEW_TERM"] = "1"

    # Put quotes around paths because they contain spaces
    python_exe = f'"{sys.executable}"'
    script_path = f'"{script}"'

    subprocess.Popen([
        "wt.exe",
        "cmd.exe",
        "/k",
        f'{python_exe} {script_path}'
    ], env=env)

    sys.exit(0)

FILE_NAME = "conversation.json"

# Load old conversation if it exists 
if os.path.exists(FILE_NAME):
    with open(FILE_NAME,"r",encoding="utf-8") as file :
        messages = json.load(file)
else :
    messages= []

print("Ai chat bot is starting ")
print("Type 'quit' to exit.\n")

while(True):
    user_msg = input("You: ")
  
    if user_msg.lower() == "quit":
        print("goodbye")
        break
    # Adding user's messges
    messages.append({
        "role":"user",
        "content" :user_msg
    })

    response = ollama.chat(
        model = "gemma3:1b",
        messages = messages
    )
    
    bot_msg = response["message"]["content"]
    
    print("Bot:",bot_msg)

    # add AI's response 

    messages.append({
        "role":"assistant",
        "content":bot_msg
    })

    # Saves conversations 
    with open (FILE_NAME,"w",encoding="utf-8") as file:
        json.dump(messages , file , indent =4 , ensure_ascii = False )