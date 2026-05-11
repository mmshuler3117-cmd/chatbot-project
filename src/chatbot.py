from src.memory import save_memory, get_memory

def run_chatbot():
    print("Chatbot waking")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Going to sleep Later!")
            break

            # simple memory trigger
        if "my name is" in user_input.lower():
            name = user_input.lower().replace("my name is", "").strip()
            save_memory("name", name)
            print(f"Chatbot: Nice to meet you, {name}! Ill remember that!")
            continue

        # recall memory
        if "what is my name" in user_input.lower():
            name = get_memory("name")
            if name:
                print(f"Chatbot: your name is {name}.")
            else: 
                print("Chatbot: I dont know your name yet..")
            continue
        print(f"Chatbot: you said '{user_input}'")
