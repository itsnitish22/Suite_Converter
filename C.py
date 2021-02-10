from gtts import gTTS               #Conversion of Google Text to Speech

name1 = input("Enter name of the file with extension:\n")

with open(name1, encoding="utf-8") as file:     #Opening the text file and reading the text
     file = file.read()

speak = gTTS(file, lang='en')                   #Speaking text to audio
speak.save("converted.mp3")                     #Saving the converted audio file

print("Your file has been converted successfully".center(400))
