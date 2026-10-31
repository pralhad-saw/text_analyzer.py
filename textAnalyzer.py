
import json
import os
HISTORY_FILE="analyzerHistory.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE,"r") as f:
            return json.load(f)
    return []
def save_history(history):
    with open(HISTORY_FILE,"w") as f:
        json.dump(history, f, indent=4)
def analyze_text(text):
    words=text.split()
    char_count=len(text)
    word_count=len(words)
    vowels= sum(1 for char in text.lower() if char in "aeiou")
    stats={
        "text_snippet": text[:30]+ ("..." if len(text)>30 else ""),
        "characters": char_count,
        "words": word_count,
        "vowels": vowels
    }
    return stats
if __name__=="__main__":
    history = load_history()
    while True:
        print("\n---CLI Text Analyzer---\n")
        print("1.Analyze New Text\n2.View History\n3.Exit.\n===made by Pralhad Kumar")
        choice = input("\n\nEnter your choice no. from option(1-3)").strip()
        if choice=="1":
            user_text=input("\nEnter Text To Analyze\n")
            if not user_text.strip():
                print("Empty Text Provided.Try Again:")
                continue
            result = analyze_text(user_text)

            print("\n===Results===\n")
            for key,val in result.items():
                print(f"{key.capitalize()}:{val}")
            history.append(result)
            save_history(history)
        elif choice=="2":
            print("\n===Past Analysis Of History===")
            if not history:
                print("\nNo History Found\n")
                continue
            else:
                for idx,items in enumerate(history,1):
                    print(f"{idx}.Words: {items['words']}, Vowels: {items['vowels']}")
        elif choice=="3":
            print("GoodBye")
            break
        else:
            print("Invalid choice .please enetr 1 2 or 3")
