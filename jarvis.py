import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")


    speak("I am jarvis I am your assistance . Please tell me how may I help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        r.energy_threshold =50
        audio = r.listen(source)
    try:
        print("Recongnizing....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    
    except Exception :
         #print(e)


        print("Say that again Please....")
        speak("Sorry I not recognised Please Say that again ")
        return "None"
    return query


def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sanidhyasaxena73@gmail.com','9045695056')
    server.sendmail('sanidhyasaxena73@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takecommand().lower()
        if 'wikipedia'in query:
            try:
             speak('Searching wikipedia....')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)
            except:
                speak("Sorry I did not found in wikipedia")
                speak("Please try again")
        elif 'open youtube' in query:
            try:
                webbrowser.open("https://www.youtube.com/")
            except:
                 speak("Sorry I did not found")
                 speak("Please try again")
        elif 'open google' in query:
            try:
                webbrowser.open("https://www.google.com/")
            except:
                 speak("Sorry I did not found")
                 speak("Please try again")
        elif 'open hackerrank' in query:
            try:
                webbrowser.open("https://www.hackerrank.com/")
            except:
                 speak("Sorry I did not found")
                 speak("Please try again")


        #elif 'play music' in query:
           #music_dir=
           #songs=os.listdir(music_dir)
           #print(songs)
           #os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The Time is {strTime}")


        elif 'open code' in query:
            codepath ="C:\\Users\\AYUSH SAXENA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to sunny' in query:
            try:
                speak("what should you say?")
                content = takecommand()
                to = "sanidhyasaxena73@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Soory sir I am unable to send this email")


   



      
           