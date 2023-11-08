import pyttsx3
import pyttsx3.voice
import speech_recognition as sr
import openai
# import json

openai.api_key = "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"

# Code found at: https://github.com/andyblarblar/ros2_tts
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

# voices = test.engine.getProperty('voices')
# for voice in voices:
#     test.engine.setProperty('voice',voice.id)
#     test.store_voice("This is a test")

# Source: https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/#
recog = sr.Recognizer()

try:
    with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source, duration = 0.2)
        
        audio = recog.listen(source, phrase_time_limit=5)
        
        text = recog.recognize_google(audio)
        text = text.lower()
        
        # Source: https://platform.openai.com/docs/guides/gpt/chat-completions-api
        # response = openai.Completion.create(
        #     model="gpt-3.5-turbo",
        #     prompt = text
        # )
        
        print("Did you say ", text)
        test = Text_To_Speech()
        test.speak(text)
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
except sr.UnknownValueError:
    print("unknown error occurred")
    
# https://platform.openai.com/docs/guides/text-generation
