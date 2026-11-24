"""
Simple Rule-Based Chatbot
Concepts used: if-elif, functions, loops, input/output
"""

import random
from datetime import datetime


def clean(text):
    """Make the user's message lowercase and remove punctuation."""
    text = text.lower().strip()
    for ch in "!?.,;:'\"":
        text = text.replace(ch, "")
    return text


def has_any(text, words):
    """Check if any word/phrase appears as a whole word in the text.
    Padding with spaces stops 'hi' from matching inside 'this'."""
    padded = " " + text + " "
    for w in words:
        if " " + w + " " in padded:
            return True
    return False


def get_reply(message):
    """Return a reply based on what the user typed."""
    text = clean(message)

    if text == "":
        return "Say something, I'm listening."

    # Exit words are checked first so they are never missed
    elif has_any(text, ["bye", "goodbye", "see you", "exit", "quit", "goodnight"]):
        return "Goodbye! Take care."

    elif has_any(text, ["how are you", "how are you doing", "how do you do", "hows it going"]):
        return "I'm fine, thanks! How about you?"

    elif has_any(text, ["hello", "hi", "hey", "hii", "yo"]):
        return random.choice(["Hi!", "Hello!", "Hey there!"])

    elif has_any(text, ["good morning"]):
        return "Good morning! Hope you have a great day."

    elif has_any(text, ["good afternoon"]):
        return "Good afternoon! How's your day going?"

    elif has_any(text, ["good evening"]):
        return "Good evening! How was your day?"

    elif has_any(text, ["your name", "who are you"]):
        return "I'm PyBot, a simple chatbot made with Python."

    elif has_any(text, ["my name is"]):
        name = text.split("my name is")[-1].strip().title()
        return "Nice to meet you, " + name + "!"

    elif has_any(text, ["what are you doing", "whats up", "sup"]):
        return "Just chatting with you. What about you?"

    elif has_any(text, ["i am fine", "im fine", "i am good", "im good", "i am great", "im great", "doing well"]):
        return "Good to hear that!"

    elif has_any(text, ["i am sad", "im sad", "i am tired", "im tired", "i am bored", "im bored"]):
        return "Sorry to hear that. Maybe take a short break or talk to a friend."

    elif has_any(text, ["thanks", "thank you", "thx"]):
        return "You're welcome!"

    elif has_any(text, ["sorry", "my bad"]):
        return "No problem at all."

    elif has_any(text, ["help"]):
        return "I can chat about simple things. Try: hello, how are you, what's the time, tell me a joke, bye."

    elif has_any(text, ["time"]):
        return "The time is " + datetime.now().strftime("%I:%M %p") + "."

    elif has_any(text, ["date", "today"]):
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."

    elif has_any(text, ["joke"]):
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the computer get cold? It left its Windows open.",
            "I would tell you a UDP joke, but you might not get it.",
        ])

    elif has_any(text, ["weather"]):
        return "I can't check the weather, but look outside the window!"

    elif has_any(text, ["food", "hungry", "eat", "lunch", "dinner", "breakfast"]):
        return "Food is great. What's your favourite dish?"

    elif has_any(text, ["music", "song"]):
        return "I like music too. Which songs do you enjoy?"

    elif has_any(text, ["love you", "like you"]):
        return "That's kind of you. I'm just a program, but thanks!"

    elif has_any(text, ["old are you", "your age"]):
        return "I was just created, so I'm very young."

    elif has_any(text, ["where are you from", "where do you live"]):
        return "I live inside your computer."

    elif has_any(text, ["yes", "yeah", "yep"]):
        return "Okay, got it."

    elif has_any(text, ["no", "nope"]):
        return "Alright."

    elif has_any(text, ["ok", "okay", "cool", "nice", "great"]):
        return "Glad you think so!"

    # Fallback when nothing matches
    else:
        return random.choice([
            "Sorry, I don't understand that yet.",
            "Hmm, I don't know how to reply to that. Type 'help' to see what I can do.",
            "Can you say that in a different way?",
        ])


def main():
    """Run the chat loop."""
    print("PyBot: Hi! I'm PyBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("PyBot:", reply)

        # Stop the loop when the user says goodbye
        if reply == "Goodbye! Take care.":
            break

if__name__=="__main__":
main()


if __name__ == "__main__":
    main()
