import json

# Load intents from JSON file
with open('chat_response.json', 'r') as file:
    intents = json.load(file)

# Function to match user input and provide the correct response
def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Iterate over each intent
    for intent in intents['intents']:
        # Check if user input matches any input in the intent
        if user_input in [inp.lower() for inp in intent['input']]:
            return intent['responses']
    
    # If no match found, return a default response
    return "Sorry, I didn't understand that."