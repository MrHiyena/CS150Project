import openai

# Set your API key
api_key = "YOUR_API_KEY"

# Initialize the OpenAI API client
openai.api_key = api_key

def ask_chatgpt(question):
    # Define the input prompt for ChatGPT
    prompt = f"You: {question}\nChatGPT:"

    # Make a request to the API
    response = openai.Completion.create(
        engine="davinci",  # Choose the GPT-3.5 engine
        prompt=prompt,
        max_tokens=50,  # Adjust the desired response length
        stop="\n",  # Stop when the model generates a newline character
    )

    # Extract and return the model's reply
    reply = response.choices[0].text.strip()
    return reply

# Example usage
question = "What is the capital of France?"
response = ask_chatgpt(question)
print("ChatGPT Response:", response)