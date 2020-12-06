from gtts import gTTS
from playsound import playsound
from webscript import normal_mes,whatssend
from pyaudio import *
from speech_recognition import *
from os import *
try:
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
    diction={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
    if "".join(times.split()).lower()=='birthdaymessage':
        getdate=What_I_Said()
        month=getdate.split()[1].lower()
        month_num=diction[month]
        date=getdate.split()[0]
        Date=date[:2]
        speak(f"Okay so {person}'s Birthday is on {Date}th {month} No problem message will be sent at 12:00 AM on that Day.")
        mess=f"Happy Birthday {person}.Enjoy the Day and Make it colorful"
        whatssend(Date,month_num,person,mess)
    elif "".join(times.split()).lower()=='anniversarymessage':
        getdate=What_I_Said()
        month=getdate.split()[1].lower()
        month_num=diction[month]
        date=getdate.split()[0]
        Date=date[:2]
        speak(f"Okay so {person}'s Anniversary is on {Date}th {month} No problem message will be sent at 12:00 AM on that Day.")
        mess=f"Happy Marriage Anniversary {person}.Enjoy the Day and Make it colorful"
    else:
        speak(f'What you want to message to {person}')
        mess=What_I_Said()
        normal_mes(person,mess)
        say(f'Your Message Has sent to {person}.You can check it')
except KeyboardInterrupt:
    pass
