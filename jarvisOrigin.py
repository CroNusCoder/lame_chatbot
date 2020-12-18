import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import googlesearch
import sys
import random
import pyautogui
import wolframalpha
#from lsHotword import ls
try:
    app = wolframalpha.Client("QEH6QH-UTYKKUEJH6")
except Exception:
    print("Some error occured")



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Just a rather very intelligent system, just give me a command, and you will love it.") 
    speak("listening to you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('parthasarathisrivastava@gmail.com','18072004partha')
    server.sendmail('parthasarathisrivastava@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    #lsHotword
    #wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'search' in query:
            speak('Searching...')
            query = query.replace("search", "")
            url = "https://www.google.com.tr/search?q={}".format(query)
            results = webbrowser.open_new_tab(url)
            speak(results)

        elif 'check on youtube' in query:
            query = query.replace("check on youtube", "")
            url = "https://www.youtube.com/results?search_query={}".format(query)
            results = webbrowser.open_new_tab(url)
            speak("which video i should play?")
            condition = takeCommand().lower()
            if 'play first video' in condition:
                pyautogui.moveTo(600, 300, duration=1)
                pyautogui.click(600, 300, duration=1)
           

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'stop' in query:
            pyautogui.press('playpause')

        elif 'open google' in query:
            speak("opening gooogle")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'check on youtube ' in query:
            query = query.replace("search", "")
            url = "https://www.youtube.com/results?search_query={}".format(query)
            results = webbrowser.open_new_tab(url)
            speak("which video i should play?")
            if 'play first video' in condition:
                pyautogui.moveTo(600, 300, duration=1)
                pyautogui.click(600, 300, duration=1)


        elif 'play music' in query:
            codePath = "C:\\Users\\parth\\music\\patlamaya.mp3"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'flip the coin' in query:
            speak('fliping the coin')
            faces=['Heads','Tails']
            x=random.choice(faces)
            speak(x)
            print(x)

        elif 'solve' in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("Internet connection  error")
                speak("Internet connection  error")

        elif 'speak about' in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("Internet connection  error")
                speak("Internet connection  error")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\parth\\Desktop\\Class bot\\gmeet_bot.py"
            os.startfile(codePath)

        elif 'open document folder' in query:
            documentfolderPath = "C:\\Users\\parth\\Documents"
            os.startfile(documentfolderPath)

        elif 'open this PC' in query:
            pcPath = "This PC"
            os.startfile(pcPath)

        elif 'open images folder' in query:
            imagesfolderPath = "C:\\Users\\parth\\Pictures"
            os.startfile(imagesfolderPath)

        elif 'play video' in query:
           videoPath = "C:\\Users\\parth\\videos\\gotcredit.mp4"
           os.startfile(videoPath)

        elif 'open illustrator' in query:
           illustratorPath = "D:\\Illustrator\\IllustratorPortable\\IllustratorCS6Portable.exe"
           os.startfile(illustratorPath)

        elif 'open photoshop' in query:
           photoPath = "D:\\Photoshop\\Photoshop.exe"
           os.startfile(photoPath)

        elif 'open last pdf' in query:
           photoPath = "C:\\Users\\parth\\Downloads\\ilovepdf_merged.pdf"
           os.startfile(photoPath)

           
        elif 'jor se bolo' in query:
           speak("jaai, maataa, diii")

        elif 'who are you' in query:
            speak("i am an Artificial Intelligent, designed and developed by Parth Sarathi Srivastava")

        elif 'email to me' in query:
            try:
                speak("emailing to you")
                speak("What should I say?")
                content = takeCommand()
                to = "parthasarathisrivastava@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")   

        elif 'close yourself' in query:
            speak("want anything else?")
        #ls.lsHotword_loop()
        
            


