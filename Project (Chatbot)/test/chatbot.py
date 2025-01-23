import json         #load responses from json file
import random       #generate and select random agents name
import logging      #records input and chatbots responses in chat_log.txt

# Set up logging
logging.basicConfig(filename='chat_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Load responses from JSON file
def load_responses(filename):   
    with open(filename, 'r') as file:
        return json.load(file)

# Generate a random agent name from the listed names
def generate_agent_name():
    names = ["Ram","Shyam","Amit","Aarin","Gopi","Ishan","Himanshu"]
    return random.choice(names)

# Get a response based on user input
def get_response(user_input, responses):
    user_input = user_input.lower()   #Converts user input to lowercase for case-insensitive matching
    for keyword in responses:
        if keyword in user_input:     #checks and returns a random response for the matching keyword
            return random.choice(responses[keyword])
    return random.choice(responses["default"])

def main():
    print("Welcome to the University of Poppleton chat system!")
    
    # Prompt for user name
    user_name = input("Please enter your name: ") #ask for name as input
    print(f"Hello, {user_name}! I'm your virtual agent today.") #displays the prompt
    
    # Display agent name
    agent_name = generate_agent_name() #generates agents name 
    print(f"Your agent today is {agent_name}.")

    # Load responses
    responses = load_responses('responses.json') #load predefined responses from the responses.json file into the responses dictionary.

    while True:
        user_question = input(f"{user_name}: ") #infinite loop for continuous chat until exit and prompt for input
        
        # Check for exit commands
        if user_question.lower() in ["bye", "quit", "exit"]:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            print("--Created By: Amit Chaudhary")
            break       #breaks the loop
        
        # Log the question
        logging.info(f"{user_name}: {user_question}")   #records the questions in chatlog
        
        # Get response
        response = get_response(user_question, responses) #calls the function for user's input
        print(f"{agent_name}: {response}")                #display response
        
        # Log the response
        logging.info(f"{agent_name}: {response}")         #records the response in chatlog

if __name__ == "__main__":  #it ensures main() function runs only when this code runs directly, 
                            # and not when it is imported into another script
    main()