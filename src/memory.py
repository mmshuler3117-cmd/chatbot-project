memory_store = {}

def save_memory(key, value):
    memory_store[key] = value

def get_memory(key):
    return memory_store.get(key, None)
