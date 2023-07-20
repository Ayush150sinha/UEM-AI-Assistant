import pyttsx3
import webbrowser
import smtplib
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import requests
from bs4 import BeautifulSoup
import pyjokes
from playsound import playsound

engine = pyttsx3.init('sapi5')


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 3 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 16:
        speak('Good Afternoon!')

    if currentH >= 16 and currentH <17:
        speak('Good Evening!')


greetMe()

speak('Hello,allow me to introduce myself, i am U E M AI ASSISTANT, a virtual artificial intelligence and am here to assist you with variety of task')
speak('How can I help you')
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('2001aratrika@gmail.com', 'grklrajesvgwphrm')
    server.sendmail('2001aratrika@gmail.com', to, content)
    server.close()


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.energy_threshold = 2000
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-IN')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))


    return query
      

if __name__ == '__main__': 

    while True:

    
        query = myCommand()
        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        
        elif 'open google' in query:
            webbrowser.open("google.com") 
       
        elif 'alarm' in query:
            speak('Enter the time for which you want to set the alarm')
            time=input("Enter the time: ")

            while True:
                Time_Ac=datetime.datetime.now()
                now=Time_Ac.strftime("%H:%M:%S")

                if now==time:
                    music_dir = "C:\\Users\\91878\\OneDrive\\Desktop\\Voice Assisstant\\music"
                    songs = os.listdir(music_dir)    
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif now>time:
                    break

        elif 'play music' in query:
            music_dir = "C:\\Users\\91878\\OneDrive\\Desktop\\Voice Assisstant\\music"
            songs = os.listdir(music_dir) 
            print(songs)   
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")  
        
        elif 'hello' in query or 'hey' in query or 'hi' in query:
            speak("Hello")      
    
        elif 'where is the library' in query:
            speak('It is in B2 ground floor')

        elif 'where is the medical room' in query:
            speak('It is in B1 ground floor,beside cafeteria')         

        elif 'where is the cafeteria' in query:
            speak('It is in B1 ground floor') 
        
        elif 'where is the financial department' in query:
            speak('It is in B1 second floor') 
            
        elif 'where is the xerox centre' in query:
            speak('It is in B1 second floor,beside dark room') 
        
        elif 'where is the physics lab' in query:
            speak('It is in B1 second floor')       
        
        elif 'where is the chemistry lab' in query:
            speak('It is in B1 second floor') 

        elif 'where is the cheap store' in query:
            speak('It is in B1 third floor')

        elif 'where is the registrar\'s office' in query:
            speak('It is in B3 ground floor')

        elif 'where is the atm' in query:
            speak('It is in B1 ground floor')

        elif 'where is the buddha auditorium' in query:
            speak('It is in B1 ground floor go straight from the main entrance')             
            
        elif 'where is the electrical lab' in query:
            speak('It is in B1 third floor room no B1 LG 3.10 right side')

        elif 'where is the electronics lab' in query:
            speak('It is in B1 third floor room no B1 LG 3.10 left side')

        elif 'where is the computer lab' in query:
            speak('There are two computer labs one is in B2 fourth floor and the other is in B1 first floor')

        elif 'where is av hall' in query:
            speak('It is in B1 fourth floor') 

        elif 'skg' in query:
            speak('It is in B3 third floor staff room')

        elif 'where is dean\'s office' in query:
            speak('It is in B1 ground floor opposite cafeteria') 

        elif 'where is the ficci auditorium' in query or 'where is B3 seminar hall' in query:
            speak('It is in B3 ground floor')  

        elif 'where is the autocad lab' in query:
            speak('It is in B3 first floor room no B3 LG 1.5') 

        elif 'where is the language lab' in query:
           speak('There are two language labs one is in B2 first floor room no B2 LG 1.3 and the other is in B1 first floor') 

        elif 'where is the biotech lab' in query:
            speak('It is in B3 second floor') 

        elif 'where is the sports room' in query:
            speak('It is in the basement') 

        elif 'where is the office' in query:
            speak('It is in B1 ground floor beside the buddha auditorium')  

        elif 'where is the innovation cell' in query:
            speak('It is in B1 third floor room number B1 LG 3.7')

        elif 'where is the clothing department' in query:
            speak('It is in B1 first floor') 

        elif 'where is examination controllers room' in query:
            speak('It is in B1 second floor')  

        elif 'where is vc\'s room' in query:
            speak('It is in B2 ground floor in the left')

        elif 'where is the mechanical workshop' in query:
            speak('It is in the basement and outside B3')

        elif 'where is the proctors room' in query:
            speak('It is in B3 corridor')  

        elif 'where is the board room' in query:
            speak('It is in B1 ground floor') 
        
        elif 'cultural' in query:
            speak('The cultural fest of Uem is called Ecstasia. It usually takes place in the month of March. ECSTASIA is a land of celebration of talents. It is a cultural fest where artists and players gather around to share their expertise with everyone. Ecstasia is filled with a lot of activities like games and sports, music, drama, dance, literacy events, fine arts, photography and even online competitions. Many colleges participate in our fest. There are exciting gifts. The last day is marked with dj night')

        elif 'about' in query:
            speak('UEM Kolkata is an engineering and management college that was established in the year 2014 by Act No 25 of 2014 of Govt of West Bengal. Being located in New Town, the Smart City of Eastern India and very near to the Netaji Subhash International Airport, the students of the University are exposed to the top corporates. UEM Kolkata has stood one out of the top 10 institutes of India including all IITs and all NITs of the country in the NPTEL program ranked by IIT Kharagpur and IIT Chennai. University of Engineering & Management (UEM) is a fully government approved and UGC recognised University. For more details visit on the link below:')
            print('https://uem.edu.in/uem-kolkata/')

        elif 'odd' in query:
            speak('It happens in the month of November to December every year for regular students and in January for backlogs')
            
        elif 'even' in query:
            speak('It happens in the month of April to May every year for regular students and in June for backlogs')

        elif 'website' in query:
            speak('The official website of UEM is www.iemcrp.com') 

        elif 'temperature' in query:
            search="temperature in kolkata"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")    

        elif 'open gmail' in query: 
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = myCommand()
                to = "2001aratrika@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email") 

        elif 'call' in query:
            from twilio.rest import Client

            account_sid='AC76e9179b450c68aceffc58dfb11a24af'
            auth_token='79520a32b847739de1431f78fe30e1ba'

            client=Client(account_sid,auth_token)

            message=client.calls \
                .create(
                    twiml='<Response><Say>Hi I am your Assisstant.How can I help you</Say></Response>',
                    from_='+13854754962',
                    to='+918789028319'
                ) 

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'nothing' in query or 'abort' in query or 'stop' or 'bye' in query:
            speak('okay')
            speak('Bye, have a good day.')
            sys.exit()    
        
        
        speak('Next Command!')