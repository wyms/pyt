def send_messages(messages, sent_messages):
    """
    Print each message and move it to the sent_messages list.
    """
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

# Example usage
text_messages = [
    "Hello there!",
    "How are you doing?",
    "Python is awesome!",
    "Keep coding!"
]

sent_messages = []
send_messages(text_messages, sent_messages)

print("\nSent Messages:")
for message in sent_messages:
    print(message)
