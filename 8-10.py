def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Example usage:
messages_list = ["Hello", "How are you?", "Python is fun!"]
sent_messages_list = []
send_messages(messages_list, sent_messages_list)

# Print both lists
print("Original Messages List:", messages_list)
print("Sent Messages List:", sent_messages_list)
