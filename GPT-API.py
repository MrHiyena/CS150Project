import openai as ai
from openai import OpenAI

# Set your API key
api_key = "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"
client = OpenAI(api_key=api_key)

# Initialize the OpenAI API client

def ask_chatgpt(question):
    # Define the input prompt for ChatGPT
    prompt = question

    # Make a request to the API
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
        messages= [
                {"role": "user", "content": prompt }
        ],
            
        # max_tokens=50,  # Adjust the desired response length
        # stop="\n",  # Stop when the model generates a newline character
    )

    # Extract and return the model's reply
    reply = response.choices[0].text.strip()
    return reply

# Example usage
question = "What is the capital of France?"
response = ask_chatgpt(question)
print("ChatGPT Response:", response)
