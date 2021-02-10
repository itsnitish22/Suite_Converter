import speech_recognition as sr     #Speech Recognition

r = sr.Recognizer() 
 
mic = sr.Microphone(device_index=0)     # define the microphone

print("Please start speaking....")      # record your speech 
with mic as source: 
   audio = r.listen(source) 
 
result = r.recognize_google(audio)      # speech recognition

with open('speechtotext.txt',mode ='w') as file:    # export the result 
   file.write(result) 

print("Your speech has been successfully converted and saved!".center(400))