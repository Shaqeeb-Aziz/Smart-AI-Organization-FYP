import cv2
import face_recognition
import xlsxwriter
from datetime import datetime
import os
from datetime import date
import pyttsx3
import threading
from vosk import Model , KaldiRecognizer
import pyaudio
#from ast import Pass


model = Model(r"D:\\Smart Ai\\vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()

stream = mic.open(format=pyaudio.paInt16, channels=1, rate= 16000, input=True, frames_per_buffer=8192 )
stream.start_stream()

model1 = Model(r"D:\\Smart Ai\\vosk-model-small-en-us-0.15")

recognizer1 = KaldiRecognizer(model, 16000)
mic1 = pyaudio.PyAudio()

stream1 = mic.open(format=pyaudio.paInt16, channels=1, rate= 16000, input=True, frames_per_buffer=8192 )
stream1.start_stream()



engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 143)
voices  = engine.getProperty('voices')

print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Engion is loading")




today = date.today()
today = today.strftime('%d:%m:%Y')
today_split  = today.split(':')
day , month , year = today_split
voice_cmd = ""
path_entrance = "D:\\smart ai files\\entrance\\"+ day + "-" + month + "-" + year
try:
    os.makedirs(path_entrance, exist_ok=False)
except FileExistsError:
    pass

Excel_sheets = "D:\\smart ai files\\entrance\\Excel sheets per day"

try:
    os.makedirs(Excel_sheets, exist_ok=False)
except FileExistsError:
    pass



speak("Camera is loading")



voice_cmd = ""
sond = "on"
def takename():
    name_return = "No name"
    print("what is your name")
    speak("what is your name")
   
    query = ""
    data  = stream.read(4096, exception_on_overflow=False)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()

        print(text[14:-3])
        query = text[14:-3]

        return query

    return name_return


def OpenListeningModule(): 
    global voice_cmd
    global sond
    speak("microphone started")


    while sond == 'on':
        
        query = ""
        data  = stream1.read(4096, exception_on_overflow=False)

        if recognizer1.AcceptWaveform(data):
            text = recognizer1.Result()
            query = text[14:-3]
        voice_cmd = query.lower()
        print(voice_cmd)
        if voice_cmd == "hi" or voice_cmd == "hello" or voice_cmd =="exit" or voice_cmd == "hey":
            sond = 'off'

            break

        if voice_cmd == "exit":
            break


        
       



file_name = "D:\\smart ai files\\entrance\\Excel sheets per day\\"+day+"-"+month+"-"+year+".xlsx"
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet()
worksheet.set_column('A:E',25)
worksheet.set_default_row(75)
cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
worksheet.write(0,0, "Person Name", cell_format)
worksheet.write(0,1, "IN-Image", cell_format)
worksheet.write(0,2, "In-Time", cell_format)
worksheet.write(0,3, "Out-Time", cell_format)



# Create the videocapture function and object
def OpenCamera():
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 430)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
    x = threading.Thread(target=OpenListeningModule, daemon=True )
    x.start()
    row = 1
    col =0
    while True:
        global voice_cmd
        global sond
        now = datetime.now()

        current_time = now.strftime("%H-%M-%S")
        voice_cmd = voice_cmd
        success, frame = cap.read()
        # Show the output


        frame = cv2.flip(frame, 1)
        image = face_recognition.face_locations(frame, model='hog')  
        face_point = list((image))

        print(face_point)
        if image != []:
            y1,x2,y2,x1 =   (face_point)[0]
            if y1 != "" and x2 != "" and y2 != "" and x1 != "":
                frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,2), 2)
            cv2.imshow("Frame", frame)
        else:
            cv2.imshow("Frame", frame)
            #Pass
    # If 'c' key is pressed then click picture
        if cv2.waitKey(1) == ord('c') or voice_cmd == "hey" or voice_cmd == "hi" or voice_cmd == "hello":
            speak("What is your name")
            #print("microphone start")
            voice_cmd =""
            speak("what is your name")
            name = input("what is your name")
            
            speak(f"{name} you can go now")
            print(f"{name} you can go now")
            file = path_entrance+'/'+ current_time + '.jpg'

 
            
            cv2.imwrite(file, frame)
            sond = "on"
            x = threading.Thread(target=OpenListeningModule, daemon=True )
            x.start()
            worksheet.write(row, col, name)
            worksheet.insert_image(row, col+1, file, {'x_scale':0.282, 'y_scale': 0.280 ,'x_offset': 0, 'y_offset': 0, 'positioning':1} )
            worksheet.write(row, col+2, current_time)
            
            
            row+=1 
            


        if cv2.waitKey(1)  == ord('q') or voice_cmd == "exit":
            break
        #print("action say: ",voice_cmd)
    workbook.close()

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    OpenCamera()
