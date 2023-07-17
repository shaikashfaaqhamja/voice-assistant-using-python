import pyttsx3
import speech_recognition as sr
import webbrowser
import asyncio
import datetime

# Initialize the speech synthesis engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
async def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = await loop.run_in_executor(None, r.listen, source)

    try:
        print("Recognizing...")
        query = await loop.run_in_executor(None, r.recognize_google, audio)
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Sorry, I couldn't understand. Please try again.")
        return ""

# Function to perform various tasks based on user commands
def perform_task(command):
    if "open youtube" in command:
        url = "https://www.youtube.com"
        speak("Yes boss!")
        webbrowser.open(url)

    elif "hello" in command:
        speak("hello boss!")
    elif "open google" in command:
        url = "https://www.google.com"
        speak("Yes boss!")
        webbrowser.open(url)
    elif "play music" in command:
        # Add your music playing code here
        pass
    elif "tell me a joke" in command:
        joke = "Why don't scientists trust atoms? Because they make up everything!"
        speak(joke)
    elif "sing" in command:
        song_name = command.split('sing', 1)[1].strip().replace("song", "").strip()
        speak(f"Sure! Searching for the music video of {song_name} on YouTube.")
        search_query = f"official music video {song_name}"  # Modify the search query as per your requirements
        url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(url)
    elif "what is the time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "exit" in command:
        speak("Goodbye!")
        loop.stop()
    else:
        speak("Sorry, I don't know how to do that.")
    

# Main program loop
async def main():
    speak("Hi, I'm EDITH. EDITH stands for even dead I am the hero. I am an advanced A.I voice assistant. How can I help you?")

    while True:
        command = await listen()
        perform_task(command)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
