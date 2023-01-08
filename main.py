# Our main file.

import speech_recognition as str

# Cria um reconhecedor
r = str.Recognizer()

# Abrir o microfone para captura
with str.Microphone() as source:
    audio = r.listen(source) # Define um microfone como fonte de áudio
    
    while True:
        print(r.recognize_google(audio, language='pt'))
        