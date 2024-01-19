def send_messages(messages, sent_messages):
    """
    Print each message and move it to the sent_messages list.
    """
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

# Assuming you have the original list of messages
original_messages = [
    "Hello there!",
    "How are you doing?",
    "Python is awesome!",
    "Keep coding!"
]

# Create a copy of the original list
archived_messages = original_messages[:]

# Call the send_messages function with the copy
sent_messages = []
send_messages(archived_messages, sent_messages)

print("\nOriginal Messages:")
for message in original_messages:
    print(message)

print("\nSent Messages:")
for message in sent_messages:
    print(message)
