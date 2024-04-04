rules = {
    "greeting": ["hi", "hello", "hey", "greetings"],
    "farewell": ["bye", "goodbye", "see you later"],
    "age_question": ["how old are you", "what's your age"],
    "joke": ["tell me a joke", "joke please"],
}

responses = {
    "greeting": "Hello! How can I assist you today?",
    "farewell": "Goodbye! Have a great day.",
    "age_question": "I'm a chatbot, so I don't have an age. How can I help you?",
    "joke": "Why couldn't the bicycle stand up by itself? It was two tired!"
}

# User input processing and rule-based responses
def chatbot_response(user_input):
    input_lower = user_input.lower()  
    
    for intent, keywords in rules.items():
        for keyword in keywords:
            if keyword in input_lower:
                return responses.get(intent)

    return "I'm not sure how to respond to that. Can you please rephrase your query?"

# Chat loop
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    # Exit loop when user says goodbye
    if response in responses["farewell"]:
        break

# End of the chatbot script
