#import library
import speech_recognition as sr
import sys
import smtplib, ssl
import os
# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable
with sr.AudioFile("male.wav") as source:
    
    audio_text = r.listen(source)    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text)
        outF = open("myOutFile.docx", "w")
        with open('myOutFile.docx', 'w') as f:
            print(text, file=f)
    except:
        print("Sorry try again") 
os.system("scp myOutFile.docx 192.168.1.5/C:\Users\Alex\Documents\speachreconition\recivefolder")