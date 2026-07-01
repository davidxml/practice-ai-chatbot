# bot.py
import random
import datetime  # NEW: Gives us access to the computer's live clock!

# Import the expanded data structure
from brain import bot_brain, fallbacks

def main():
    print("====================================")
    print("Bot powered on. Type 'quit' to exit.")
    print("====================================")

    while True:
        user_text = input("\nYou: ")
        cleaned_text = user_text.lower().strip()
        
        if cleaned_text == "quit":
            print("Bot: Powering down. Goodbye!")
            break
            
        # --- DYNAMIC SYSTEM CHECK ---
        # This checks for a specific question and runs a live function
        if "time" in cleaned_text:
            # Ask the operating system for the current hour and minute
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Bot: The current system time is {current_time}.")
            continue # Skip the dictionary check and restart the loop
            
        # --- THE LOGIC ROUTING ---
        match_found = False
        
        for keyword in bot_brain:
            if keyword in cleaned_text:
                response = random.choice(bot_brain[keyword])
                print(f"Bot: {response}")
                match_found = True
                break 
                
        # --- GRACEFUL FAILURE ---
        if not match_found:
            response = random.choice(fallbacks)
            print(f"Bot: {response}")

if __name__ == "__main__":
    main()

