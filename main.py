while True:
    command = input("You: ").lower()

    if "call" in command:
        print("Luna: Calling contact 📞")
    elif "bluetooth" in command:
        print("Luna: Bluetooth connected 🔵")
    elif "exit" in command:
        print("Luna: Goodbye 🌙")
        break
    else:
        print("Luna: I did not understand")

