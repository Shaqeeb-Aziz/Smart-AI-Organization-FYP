from deepface import DeepFace
import face_recognition
import cv2
import mysql.connector as sqlconnect
from datetime import date
import pyttsx3
import datetime
import os
from datetime import datetime
import threading
import logging
from vosk import Model , KaldiRecognizer
import pyaudio
#import speech_recognition as sr


model = Model(r"D:\\Smart Ai\\vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()

stream = mic.open(format=pyaudio.paInt16, channels=1, rate= 16000, input=True, frames_per_buffer=8192 )
stream.start_stream()





today = date.today()
today = today.strftime('%d:%m:%Y')
today_split  = today.split(':')
day , month , year = today_split
day  = int(day)
month = int(month)
year = int(year)
d1 = date(year, month, day)
print(day , month , year)

conn = sqlconnect.connect(host= 'localhost',user='root',password='',database='receptionist')
D = str(day)
M = str(month)
Y = str(year)
mycursor= conn.cursor()
path_interview = "D:\\smart ai files\\interview\\"+D+"-"+M+"-"+Y
try:
    os.makedirs(path_interview, exist_ok=False)
except FileExistsError:
    pass

voice_cmd = ""
sond = "on"

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(gender):
     
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {gender}")

    elif hour >= 12 and hour< 18 :
        speak(f"Good afternoon {gender}")

    else:

        speak(f"Good Evening {gender}")        




def OpenListeningModule():  
    logging.info("Opening Microphone")
    global voice_cmd
    global sond
    speak("microphone started")
    while True:
        
        while sond == 'on':
            query = " "
            
            data  = stream.read(4096, exception_on_overflow=False)

            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()

                print(text[14:-3])
                query = text[14:-3]
                #return query

                
            voice_cmd = query.lower()
            print(voice_cmd)
            if voice_cmd == "hi" or voice_cmd == "hello" or voice_cmd == "hey":
                sond = 'off'

                break




def model_predict():
    img1 = cv2.imread('D:\m1.jpg')
    result = DeepFace.analyze(img1, actions=['gender'])
    print(result)
    gender = result.get('gender')
    gender = gender.lower()
    print(gender)

    return gender


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 244)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 244)

today_date = D+":"+M+":"+Y
query = (f"select * from interview WHERE  date_visit = '{today_date}'")

print(query)
result = mycursor.execute(query, today_date)
select = mycursor.fetchall()

tic_number = len(select)+1

print("token start with",tic_number)

def OpenCamera():

    global tic_number
    global date

    x = threading.Thread(target=OpenListeningModule, daemon=True )
    x.start()



    while True:
        while True:
            global voice_cmd
            global sond
            _, frame = cap.read()
            frame = cv2.flip(frame,1)
            cv2.imshow("image",frame)

            if cv2.waitKey(1)== ord('c') or voice_cmd == "hey" or voice_cmd == "hi" or voice_cmd == "hello":
                sond = 'off'
                break

        
        
        Answer = ""
        lst = str(tic_number)
        ticket = lst

        

        face = face_recognition.face_locations(frame, model='hog')
        print("1 ", face)
        if face != []:
            voice_cmd =""
            file = 'D:\m1.jpg'

 
            
            cv2.imwrite(file, frame)
            flag , image = cap.read()
            
            prediction = model_predict()
            print(prediction)
            
            if prediction == 'woman':
                gender = "female"
                Answer = 'MAM'

            elif prediction == 'man':
                gender = "male"
                Answer = 'SIR'

            wishme(Answer)

            speak("How my i assist you:")
            #greeting  = takeCommand().lower()
            greeting = input("How may i Assist you:")
            print(greeting)
            if  'interview' in greeting:
                speak("Please write your CNIC Number without Dashes:")
                print("Please write your CNIC Number without Dashes:")
                cnic = input()

                cnic_split = cnic.split()
                cnic ="" 
                for i in cnic_split:
                    cnic= cnic+i
                    print(cnic)
                
                print("cnic" , cnic)
                while len(cnic) != 13:
                    speak("Please write correct CNIC number That is 13 Digit long:")
                    cnic = input()
                    cnic_split = cnic.split()
                    cnic =""
                    for i in cnic_split:
                        cnic= cnic+i
                    print(cnic)

                
                query = 'select name, date_visit from interview where cnic = ' +str(cnic)+ ''   

                result = mycursor.execute(query)
                select = mycursor.fetchall()


                print(select)
        
                if  select ==[]:
                    speak("What is your good name?")
                    question = "What is your good name?"
                    #user_told = takeCommand().lower()
                    user_told = input("what is your name?")
                    name = user_told

                    gender = gender
                    #date   = today

                    speak("Please tell me your qualification: ")
                    question = "Please tell your qualification:"
                    #user_told = takeCommand().lower()
                    
                    user_told = input("what is your name")
                    education = user_told


                    speak("which isntitue you were studied: ")
                    question = "Please tell your qualification:"
                    #user_told = takeCommand().lower()
                    user_told = input("which isntitue you were studied: ")
                    institute = user_told

                    purpose = "Interview"

                    
                    tic_number = int(tic_number)+1
                    speak(f'welcome to Smart AI Organisation your ticket number is {ticket}:')
                    query = "INSERT INTO interview VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s , %s)  "
                    values = (name, gender ,cnic, today_date , education , institute ,purpose , ticket )

                    mycursor.execute(query, values)
                    conn.commit()
                    file = path_interview+"\\"+ticket+'.jpg'
                    cv2.imwrite(file, frame)
                    
                    sond = 'on'
                elif select != []:
                    for i in select:
                        name = list(i)[0]
                        date_visit = list(i)[1]

                    date_visit  = date_visit.split(':')
                    print("last Visit was:", date_visit)
                    day_visit , month_visit , year_visit = date_visit
                    day_visit  = int(day_visit)
                    month_visit = int(month_visit)
                    year_visit = int(year_visit)
                
                    d0 = date(year_visit, month_visit, day_visit)
                    delta = d1 - d0
                    print(delta.days)
                    if delta.days <= 90:
                        speak(f"Dear {name} sorry to inform you that you are not illegible for intervie")
                        speak(f"Because you already gave interview {delta.days} Days ago" )
                        speak("Please try again after 90 days")

                    elif delta.days >90:
                        speak("you may now give interview")
                    
                        sql_updat = "UPDATE interview SET date_visit = %s , ticket = %s WHERE cnic = %s"
                        values = (today, ticket ,cnic)
                        mycursor.execute(sql_updat, values)

                        conn.commit()
                        file = path_interview+"\\"+ticket+'.jpg'
                        cv2.imwrite(file, frame)
                        print(sql_updat)
                        tic_number = tic_number + 1

                    sond ='on'

            elif greeting == 'orientation':
                day = datetime.today().strftime('%A').lower()

                if day == 'saturday':
                    speak("GO to confrance room and orientation will be star at 10PM:")

                else:
                    speak("please Reach on Orientation day that is on Saturday")
                
                sond = 'on'
            else:
                speak(f"sorry {Answer} i an not able to help you with this:")

                sond = 'on'



if __name__ == "__main__":
    OpenCamera()



