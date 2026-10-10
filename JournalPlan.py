import os
from datetime import datetime
import random

class Entry:
    
    def __init__(self, date: str, prompt_text: str, entry_text: str):
        self.date = date
        self.prompt_text = prompt_text
        self.entry_text = entry_text

    def display(self):
        print(f"Date: {self.date} - Prompt: {self.prompt_text}")
        print(f"{self.entry_text}\n")


class PromptGenerator:
    
    def __init__(self):
        self._prompts = [
            "Who was the most interesting person I interacted with today?",
            "What was the best part of my day?",
            "How did I see the hand of the Lord in my life today?",
            "What was the strongest emotion I felt today?",
            "If I had one thing I could do over today, what would it be?",
            "What is a small win I experienced today?",
            "What challenged me today and how did I handle it?"
        ]

    def get_random_prompt(self) -> str:
        return random.choice(self._prompts)


class Journal:
    
    def __init__(self):
        self._entries = []

    def add_entry(self, new_entry: Entry):
        self._entries.append(new_entry)

    def display_all(self):
        if not self._entries:
            print("The journal is currently empty.\n")
            return
            
        for entry in self._entries:
            entry.display()

    def save_to_file(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            for entry in self._entries:
                # Using '~|~' as a separator to safely handle symbols inside text
                file.write(f"{entry.date}~|~{entry.prompt_text}~|~{entry.entry_text}\n")

    def load_from_file(self, filename: str):
        if os.path.exists(filename):
            self._entries.clear()
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split("~|~")
                        if len(parts) == 3:
                            entry = Entry(parts[0], parts[1], parts[2])
                            self._entries.append(entry)
        else:
            print(f"Error: The file '{filename}' was not found.\n")


def main():
    journal = Journal()
    prompt_gen = PromptGenerator()
    
    while True:
        print("Please select one of the following choices:")
        print("1. Write a new entry")
        print("2. Display the journal")
        print("3. Save the journal to a file")
        print("4. Load the journal from a file")
        print("5. Quit")
        
        choice = input("What would you like to do? ")

        if choice == "1":
            prompt = prompt_gen.get_random_prompt()
            print(f"\nPrompt: {prompt}")
            response = input("> ")
            current_date = datetime.now().strftime("%m/%d/%Y")
            
            new_entry = Entry(current_date, prompt, response)
            journal.add_entry(new_entry)
            print("Entry added successfully!\n")

        elif choice == "2":
            print("\n--- Journal Entries ---")
            journal.display_all()

        elif choice == "3":
            filename = input("Enter filename to save (e.g., journal.txt): ")
            journal.save_to_file(filename)
            print("Journal saved!\n")

        elif choice == "4":
            filename = input("Enter filename to load: ")
            journal.load_from_file(filename)
            print("Journal loaded!\n")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
