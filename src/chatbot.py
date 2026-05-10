import kson
import os

MEMORY_FILE = "memory.json"

# load Memory if it exists
if os.path.exists(MEMORY_FILE):
	with open(MEMORY_FILE, "r") as f:
		memory = json.load(f)
else: 
	memory = {}

print("Chatbot: I'm back. I remember thing now.")

while True:
	user = input("You: ").lower()
print("Chatbot: I'm back. I remember nothing... yet.")

name = None

while True:
    user = input("You: ").lower()

    if user == "quit":
        print("Chatbot: Goodbye.")
        break

    elif "my name is" in user:
        name = user.replace("my name is", "").strip()
        print(f"Chatbot: Got it. I'll remember {name}.")

    elif "what is my name" in user:
        if name:
            print(f"Chatbot: You told me your name is {name}.")
        else:
            print("Chatbot: You haven't told me yet.")

    elif "hello" in user or "hi" in user:
        if name:
            print(f"Chatbot: Hey {name}.")
        else:
            print("Chatbot: Hey.")

    else:
        print("Chatbot: I don't know how to respond to that yet.")
