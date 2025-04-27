from gtts import gTTS

text = '''Ваш текст для озвучки'''

tts = gTTS(text=text, lang='ru')

tts.save('output.mp3')
