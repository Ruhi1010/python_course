#8.10
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)


text_messages = [
    "Hello, how are you?",
    "Nice to meet you"
    "Don't forget me"
]


sent_messages = []


send_messages(text_messages, sent_messages)


print("\nRemaining messages:", text_messages)
print("Sent messages:", sent_messages)
