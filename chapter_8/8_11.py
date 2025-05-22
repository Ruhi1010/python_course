#8.11
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

text_messages = [
    "Hello, how are you?",
    "Nice to meet you.",
    "Don't forget me."
]

text_messages_copy = text_messages.copy()

sent_messages = []

send_messages(text_messages_copy, sent_messages)

print("\nOriginal messages:", text_messages)
print("Sent messages:", sent_messages)
