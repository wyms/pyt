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
