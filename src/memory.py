import json
import os

MEMORY_FILE = "src/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "name": None,
            "preferences": [],
            "facts": []
        }

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


# --- NAME ---
def set_name(name):
    memory = load_memory()
    memory["name"] = name
    save_memory(memory)


def get_name():
    memory = load_memory()
    return memory.get("name")


# --- PREFERENCES ---
def add_preference(item):
    memory = load_memory()
    memory["preferences"].append(item)
    save_memory(memory)


# --- FACTS ---
def add_fact(fact):
    memory = load_memory()
    memory["facts"].append(fact)
    save_memory(memory)