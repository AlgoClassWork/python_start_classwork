import pyttsx3

def getVoice(voices):
    for voice in voices:
        if 'ru' in voice.languages[0]:
            return voice

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

voices = engine.getProperty('voices')
ru_voice = getVoice(voices)
engine.setProperty('voice', ru_voice.id)

engine.save_to_file('Привет, как дела?', 'test.aiff')
engine.runAndWait()
