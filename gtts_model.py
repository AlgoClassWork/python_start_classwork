from gtts import gTTS

text = '''Почему программист никогда не тонет?
— Потому что он всегда всплывает в отладке! 😄'''

sound = gTTS(text=text, lang='it')
sound.save('sound.mp3')
