import json
import os
import random
import tkinter as tk
from tkinter import scrolledtext

# Load intents from JSON file safely
def load_intents(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file location.")
        exit()
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' is not a valid JSON file.")
        exit()

# Execute system commands
def execute_command(tag, user_input):
    if tag == "shutdown":
        os.system("shutdown /s /t 0")  # Shutdown PC
    elif tag == "restart":
        os.system("shutdown /r /t 0")  # Restart PC
    elif tag == "sleep":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Sleep mode
    elif tag == "lock":
        os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock screen
    elif tag == "logoff":
        os.system("shutdown /l")  # Log out
    elif tag == "open_application":
        if "chrome" in user_input:
            os.system("start chrome")
        elif "firefox" in user_input:
            os.system("start firefox")
        elif "notepad" in user_input:
            os.system("start notepad")
        elif "word" in user_input:
            os.system("start winword")
        elif "excel" in user_input:
            os.system("start excel")
        elif "command prompt" in user_input or "cmd" in user_input:
            os.system("start cmd")
        elif "calculator" in user_input:
            os.system("start calc")
        elif "paint" in user_input:
            os.system("start mspaint")
        else:
            chat_display.insert(tk.END, "Chatbot: I couldn't recognize the application.\n")
    elif tag == "increase_volume":
        os.system("nircmd.exe changesysvolume 2000")  # Increase volume (requires NirCmd)
    elif tag == "decrease_volume":
        os.system("nircmd.exe changesysvolume -2000")  # Decrease volume
    elif tag == "mute":
        os.system("nircmd.exe mutesysvolume 1")  # Mute system
    elif tag == "unmute":
        os.system("nircmd.exe mutesysvolume 0")  # Unmute system
    else:
        chat_display.insert(tk.END, f"Chatbot: Command '{tag}' not recognized.\n")

# Match user input with an intent
def get_intent(user_input, intents):
    user_input = user_input.lower()
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if user_input == pattern.lower():
                return intent["tag"]
    return None  # No matching intent found

# Process user input
def process_input():
    user_input = user_entry.get().strip().lower()
    if user_input == "":
        return
    
    chat_display.insert(tk.END, f"You: {user_input}\n")

    if user_input in ["exit", "quit", "bye"]:
        chat_display.insert(tk.END, "Chatbot: Goodbye!\n")
        root.quit()
        return

    intent_tag = get_intent(user_input, intents)

    if intent_tag:
        system_commands = ["shutdown", "restart", "sleep", "lock", "logoff", "open_application", "increase_volume", "decrease_volume", "mute", "unmute"]
        
        if intent_tag in system_commands:
            execute_command(intent_tag, user_input)  # 🔥 FIXED: Now passing `user_input`
            chat_display.insert(tk.END, f"Chatbot: Executing '{intent_tag}' command...\n")
        else:
            # If it's a normal conversation intent, respond normally
            for intent in intents["intents"]:
                if intent["tag"] == intent_tag:
                    response = random.choice(intent["responses"])  # Pick a random response
                    chat_display.insert(tk.END, f"Chatbot: {response}\n")
                    break
    else:
        chat_display.insert(tk.END, "Chatbot: I don't understand that command.\n")

    user_entry.delete(0, tk.END)  # Clear input field

# GUI Setup
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x500")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state="normal")
chat_display.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=50)
user_entry.pack(padx=10, pady=5)
user_entry.bind("<Return>", lambda event: process_input())

send_button = tk.Button(root, text="Send", command=process_input)
send_button.pack(pady=5)

# Ensure correct JSON file path
json_file_path = os.path.join(os.path.dirname(__file__), "intents.json")

# Load the intents file
intents = load_intents(json_file_path)

# Run the GUI
root.mainloop()
