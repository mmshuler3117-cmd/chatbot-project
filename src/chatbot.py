from src.memory import set_name, get_name, add_preference, add_fact

def run_chatbot():
    print("Vex waking")

# memory logic
    while True:
        user_input = input("You: ").lower()

        if user_input in ["exit", "quit"]:
            print("Vex: Going to sleep Later!")
            break

            # name logic
        if "my name is" in user_input:
            name = user_input.replace("my name is", "").strip()
            set_name(name)
            print(f"Vex: Nice to meet you, {name}! Ill remember that!")
            continue

        if "what is my name" in user_input:
            name = get_name()
            if name:
                print(f"Vex: You are: {name}.")
            else:
                print("Vex: We are not aquanted yet.")
            continue

        #preferences

        if "i like" in user_input:
            thing = user_input.split("i like")[-1].strip()
            add_preference(thing)
            print(f"Vex: Got it. you like{thing}. Ill remember.")
            continue

            # facts
        if "i am" in user_input:
            fact = user_input.split("i am")[-1].strip()
            add_fact(fact)
            print(f"Vex: Noted. You are {fact}.")
            continue

            #Desfault
        print(f"Vex:: you said '{user_input}'")
