chat = []
END_COMMAND = 'end'

while True:
    command = input().split()

    if command[0] == END_COMMAND:
        break

    if command[0] == "Chat":
        message = command[1]
        chat.append(message)

    elif command[0] == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)
        else:
            continue

    elif command[0] == "Edit":
        original_message = command[1]
        edited_message = command[2]
        if original_message in chat:
            original_message_index = chat.index(original_message)
            chat[original_message_index] = edited_message
        else:
            continue

    elif command[0] == "Pin":
        message = command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
        else:
            continue

    elif command[0] == "Spam":
        spam_messages = command[1:]
        chat.extend(spam_messages)

chat_history = '\n'.join(chat)
print(chat_history)