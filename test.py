from openai import OpenAI
import pyttsx3
import speech_recognition as sr

# Set your API key
api_k = "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"
client = OpenAI(api_key=api_k)

# Source: https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/#
def get_user_command():
    recog = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recog.adjust_for_ambient_noise(source, duration = 0.2)
            
            audio = recog.listen(source, phrase_time_limit=5)
            
            text = recog.recognize_google(audio)
            text = text.lower()
            
            print("Did you say ", text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
        
    return text

# Source: https://platform.openai.com/docs/guides/text-generation
def ask_chatgpt(text):
    # Define the input prompt for ChatGPT
    prompt = text

    # Make a request to the API
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
        messages= [
                {"role": "user", "content": prompt }
        ],
    )

    # Extract and return the model's reply
    reply = str(response.choices[0].message.content)
    return reply

# Our own code
question = get_user_command()
reply = ask_chatgpt(question)

# Source: https://github.com/andyblarblar/ros2_tts
class Text_To_Speech():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', '1')
        self.engine.setProperty('rate', 110)
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        
    def store_voice(self,text):
        self.engine.save_to_file(text, 'text.mp4')
        self.engine.runAndWait()


test = Text_To_Speech()
test.speak(reply)