import openai

# Set your API key (best to use an environment variable for this)
api_key = "sk-yourapikey"
openai.api_key = api_key

def ask_chatgpt(question):
    # Define the input prompt for ChatGPT
    prompt = question

    # Make a request to the API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        # Uncomment below if needed
        # max_tokens=50,  # Adjust the desired response length
        # stop="\n",  # Stop when the model generates a newline character
    )

    # Extract and return the model's reply
    # Assuming this is how the API structure looks, verify with actual API documentation
    reply = response['choices'][0]['message']['content'].strip()
    return reply

# Example usage
question = "What is the capital of France?"
response = ask_chatgpt(question)
print("ChatGPT Response:", response)
