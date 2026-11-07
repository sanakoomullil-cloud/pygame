import random


rules = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What are we working on?",
        "Hey! Great to see you.",
        "Greetings! Ready to code?"
    ],
    "help": [
        "I'm here to assist! What's tripping you up?",
        "Let's figure it out together. What do you need?",
        "Sure thing! Tell me what's going on."
    ],
    "fallback": [
        "Hmm, I didn't quite catch that. Could you rephrase?",
        "I'm a strict rule-based bot and don't know that phrase yet!",
        "Could you try asking that a different way?"
    ]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    

    if any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
        return random.choice(rules["greeting"])
        
    # Check for help keywords
    if any(word in user_input for word in ["help", "stuck", "assist"]):
        return random.choice(rules["help"])
        
    
    return random.choice(rules["fallback"])

def main():
    print("🤖 Chatbot: Booting up with random response matrices...")
    print("🤖 Chatbot: Say hello to begin! (Type 'exit' to quit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            print("🤖 Chatbot: Goodbye!")
            break
            
        response = get_response(user_input)
        print(f" Chatbot: {response}\n")

if __name__ == "__main__":
    main()
