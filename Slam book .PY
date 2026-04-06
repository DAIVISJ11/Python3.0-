import json

def create_slam_entry():
    print("--- ✨ Digital Slam Book 2026 ✨ ---")
    
    # Define the questions
    entry = {
        "Name": input("What's your name? "),
        "Nickname": input("What do your friends call you? "),
        "Favorite Color": input("What color defines your soul? "),
        "Hobby": input("What do you do for fun? "),
        "Dream Job": input("What's your 2026 career goal? "),
        "Message": input("Leave a message for the owner: ")
    }
    
    save_entry(entry)
    print("\nEntry saved! Thanks for being awesome.")

def save_entry(data):
    try:
        # Load existing data first
        try:
            with open("slambook.json", "r") as file:
                entries = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            entries = []

        # Add new entry and save
        entries.append(data)
        with open("slambook.json", "w") as file:
            json.dump(entries, file, indent=4)
            
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

if __name__ == "__main__":
    create_slam_entry()