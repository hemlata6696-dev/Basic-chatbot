# PyBot: Simple Rule-Based Chatbot in Python

PyBot is a beginner-friendly chatbot that replies to everyday messages using fixed rules. It has no AI and needs no internet. It reads what you type, looks for known words, and gives a matching reply.

## Features

- Greets you and says goodbye
- Answers small talk like "how are you"
- Remembers your name when you say "my name is..."
- Tells the current time and date
- Tells random jokes
- Chats about food, music, weather and more
- Gives a polite reply when it doesn't understand

## Concepts Used

- `if-elif` statements to pick the right reply
- Functions to keep the code clean and reusable
- `while` loop to keep the chat running
- `input()` and `print()` for user interaction
- `random` and `datetime` modules

## Requirements

- Python 3.6 or higher
- No extra libraries needed

## How to Run

1. Download or clone this repository:
   ```
   git clone https://github.com/YOUR-USERNAME/python-rule-based-chatbot.git
   ```
2. Go into the folder:
   ```
   cd python-rule-based-chatbot
   ```
3. Run the chatbot:
   ```
   python chatbot.py
   ```
4. Type `bye` to exit.

## Sample Conversation

```
PyBot: Hi! I'm PyBot. Type 'bye' to exit.
You: hello
PyBot: Hey there!
You: how are you?
PyBot: I'm fine, thanks! How about you?
You: my name is Sam
PyBot: Nice to meet you, Sam!
You: what is the time
PyBot: The time is 10:43 AM.
You: bye
PyBot: Goodbye! Take care.
```

## How It Works

1. The user types a message.
2. `clean()` makes it lowercase and removes punctuation.
3. `get_reply()` checks the message against each rule using `if-elif`.
4. The first matching rule gives the reply.
5. If nothing matches, a fallback reply is shown.
6. The loop repeats until the user says goodbye.

## Limitations

- It only understands the keywords written in the code
- It has no memory of earlier messages
- The first matching rule wins, so the order of rules matters

## Future Improvements

- Use the saved name in later replies
- Add more topics and replies
- Move replies into a dictionary for easier editing

## Author

Your Name
