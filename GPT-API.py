import openai as ai
from openai import OpenAI

# Set your API key
api_k = "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"
client = OpenAI(api_key=api_k)

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
    # reply = response.choices[0].text.strip()
    reply = str(response.choices[0].message.content)
    return reply

# Example usage
question = "What is the capital of France?"
reply = ask_chatgpt(question)
print("ChatGPT Response:"+ reply)
