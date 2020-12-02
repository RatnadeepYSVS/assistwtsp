from gtts import gTTS
from playsound import *
from pyaudio import *
from speech_recognition import *
from webscript import normal_mes,whatssend
from os import *
def greet(text):
    greeting=gTTS(text=text,lang='en')
    greeting.save('greet.mp3')
    playsound('greet.mp3')
    remove('greet.mp3')
def speak(text):
    file=gTTS(text=text,lang='en')
    file.save('anothertest.mp3')
    playsound('anothertest.mp3')
    remove('anothertest.mp3')
def select(option):
    anofile=gTTS(text=option,lang='en')
    anofile.save('option.mp3')
    playsound('option.mp3')
    remove('option.mp3')
def say(text):
    says=gTTS(text=text,lang='en')
    says.save('say.mp3')
    playsound('say.mp3')
    remove('say.mp3')
def What_I_Said():
    r=Recognizer()
    said=''
    with Microphone() as source:
        print('Listening')
        audio=r.listen(source,phrase_time_limit=5)
        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception:
            said='Error.There is a Problem With Your Microphone.'
    return said  
greet("Welcome.My name is Rose.Usage is Simple Here.Just Say the person's name and what type of message whether its a birthday or anniversary message u want to message.")
person=What_I_Said()
times=What_I_Said()
if "".join(times.split()).lower()=='birthdaymessage':
    speak(f"Okay so today is {person}'s Birthday No problem message will be sent at 12:00 AM Tonight.")
    mess=f"Happy Birthday {person}.Enjoy the Day and Make it colorful"
    whatssend(person,mess)
elif "".join(times.split()).lower()=='anniversarymessage':
    speak(f"Okay so today is {person} anniversary No problem message will be sent at 12:00 AM Tonight")
    mess=f"Happy anniversary {person}.Enjoy the Day and Make it colorful."
    whatssend(person,mess)
else:
    speak(f'What you want to message to {person}')
    mess=What_I_Said()
    normal_mes(person,mess)
    say(f'Your Message Has sent to {person}.You can check it')
    