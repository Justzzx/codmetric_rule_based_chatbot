def rule_based_chatbot():
    print("Chatbot: Hello! I am Justin's AI Assistant.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["exit", "bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! Nice to meet you.")

        elif "how are you" in user_input:
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("Chatbot: I am Justin's Rule-Based AI Chatbot.")

        elif "ai" in user_input:
            print("Chatbot: AI stands for Artificial Intelligence.")

        elif "python" in user_input:
            print("Chatbot: Python is a popular programming language used in AI.")

        elif "help" in user_input:
            print("Chatbot: You can ask about AI, Python, my name, or greetings.")

        else:
            print("Chatbot: Sorry, I don't understand that.")

rule_based_chatbot()