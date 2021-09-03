#pip install SpeechRecognition
import speech_recognition as sr
from gtts import gTTS
import playsound
import os


#this function takes voice input from the person 
# in this the source is the microphone of your system 
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening..")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data


#This function converts text which is passed as an argument to speech
def respond(String):
    print(String)
    tts = gTTS(text=String,lang="en")
    tts.save("speech.mp3")
    playsound.playsound("speech.mp3")
    os.remove("speech.mp3")



#This function displays output according to the voice input given by the person
def voice_assistant(data):
   
        if "ground floor" in data:
            listening =True
            respond("ground floor")
            if current != 0:
                lst.append(0)

            respond('any other floor')
        if "first floor" in data:
            listening =True
            respond("first floor")
            if current != 1:
                lst.append(1)
            
            respond('any other floor')
        if ("second floor") in data:
            listening =True
            respond("second floor")
            if current != 2:
                lst.append(2)
            respond('any other floor')
        if ("2nd floor") in data:
            listening =True
            respond("second floor")
            if current != 2:
                lst.append(2)
            respond('any other floor')
        if "third floor" in data:
            listening =True
            respond("third floor")
            if current != 3:
                lst.append(3)
            respond('any other floor')
        if "3rd floor" in data:
            listening =True
            respond("third floor")
            if current != 3:
                lst.append(3)
            respond('any other floor')
        if "forth floor" in data:
            listening =True
            respond("forth floor")
            if current != 4:
                lst.append(4)
            respond('any other floor')
        if "4th floor" in data:
            listening =True
            respond("forth floor")
            if current != 5:
                lst.append(5)
            respond('any other floor')
        if "fifth floor" in data:
            listening =True
            respond("fifth floor")
            if current != 5:
                lst.append(5)
            respond('any other floor')
        if "5th floor" in data:
            listening =True
            respond("fifth floor")
            if current != 5:
                lst.append(5)
            respond('any other floor')
        if "sixth floor" in data:
            listening =True
            respond("sixth floor")
            if current != 6:
                lst.append(6)
            respond('any other floor')
        if "6th floor" in data:
            listening =True
            respond("sixth floor")
            if current != 6:
                lst.append(6)
            respond('any other floor')
        if "seventh floor" in data:
            listening =True
            respond("seventh floor")
            if current != 7:
                lst.append(7)
            respond('any other floor')
        if "7th floor" in data:
            listening =True
            respond("seventh floor")
            if current != 7:
                lst.append(7)
            respond('any other floor')
        if "eighth floor" in data:
            listening =True
            respond("eighth floor")
            if current != 8:
                lst.append(8)
            respond('any other floor')
        if "8th floor" in data:
            listening =True
            respond("eighth floor")
            if current != 8:
                lst.append(8)
            respond('any other floor')
        if "nineth floor" in data:
            listening =True
            respond("nineth floor")
            if current != 9:
                lst.append(9)
            respond('any other floor')
        if "9th floor" in data:
            listening =True
            respond("nineth floor")
            if current != 9:
                lst.append(9)
            respond('any other floor')
        if "no" in data:
            listening = False
            print("Listening Stopped")
            respond("okay")

        try:
            return listening
        except UnboundLocalError:
           
            respond('Sorry no floors recognized lets try again')
            respond("Where do you want to go?")
            listening = True
            while listening == True:
                data = listen()
                listening = voice_assistant(data)


#This function controls the functionality of the assistant inside the elevator
def start_assistant(start):
    if "Alpha" in start:
        respond("Hello! Where do you want to go?")
        listening = True
        while listening == True:
            data = listen()
            listening = voice_assistant(data)
    else:
        listening = True
        while listening == True:
            start = listen()
            listening=start_assistant(start)


def voice_assistant_outside(data):
   
        if "up" in data:
            
            listening =False
            respond("up")
            upward = True
            respond("Please wait the elevator is coming")
           
        if "down" in data:
            listening =False
            respond("down")
            downward = True
            respond("Please wait the elevator is coming")
            
        try:
            return listening
        except UnboundLocalError:
           
            respond('Sorry could not recognize lets try again')
            respond("Where do you want to go? Up or Down")
            listening = True
            while listening == True:
                data = listen()
                listening = voice_assistant_outside(data)


#This function controls the functionality of the assistant outside the elevator
def start_assistant_outside(start):
    if "Alpha" in start:
        respond("Hello! Where do you want to go? Up or Down")
        listening = True
        while listening == True:
            data = listen()
            listening = voice_assistant_outside(data)
    else:
        listening = True
        while listening == True:
            start = listen()
            listening=start_assistant_outside(start)

lst=list()


#taking the below input to get an idea that the person is calling the lift from which floor
current=int(input("Enter your current floor number "))

#The virtual assistant won't get activated unless you say its name "Alpha"
#The below block of code asks the person whether he wants to go up or down
# This is outside the elevator
print("Say Alpha to begin")
listening = True
while listening == True:
    start = listen()
    listening=start_assistant_outside(start)


#Once the elevator comes and the person gets in and after the door is closed the below code is executed
#This is inside the elevator
print("Say Alpha to begin")
listening = True
while listening == True:
    start = listen()
    listening=start_assistant(start)

if current == 0:
    lst.sort()
    
if current == 9:
    lst.sort(reverse=True)
    

print("The order in which the floors are traversed")
for i in lst:
    print(i)


    

        
    



