def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Example usage:
messages_list = ["Hello", "How are you?", "Python is fun!"]
sent_messages_list = []

# Creating a copy of the original messages list
messages_copy = messages_list.copy()

# Calling send_messages with the copy
send_messages(messages_copy, sent_messages_list)

# Print both lists
print("Original Messages List:", messages_list)
print("Sent Messages List:", sent_messages_list)
