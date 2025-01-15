import json
import random
import time
import os

# Constants
EVENT_TYPES = ["view", "click", "purchase"]
PRODUCTS = ["Laptop", "Smartphone", "Tablet", "Headphones", "Camera"]
USERS = [f"user_{i}" for i in range(1, 11)]

def generate_event():
    """Simulates a user interaction event."""
    return {
        "user_id": random.choice(USERS),
        "event_type": random.choice(EVENT_TYPES),
        "product": random.choice(PRODUCTS),
        "timestamp": int(time.time())
    }

def save_to_file(events, directory="data/raw"):
    """Saves multiple events as a single JSON file."""
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"events_{int(time.time())}.json")
    with open(file_path, 'w') as file:
        json.dump(events, file, indent=4)
    print(f"Events saved: {file_path}")

if __name__ == "__main__":
    events = []
    for _ in range(10):  # Generate 10 events
        event = generate_event()
        events.append(event)
        time.sleep(1)  # Simulate time between events

    save_to_file(events)  # Save all events to a single file
