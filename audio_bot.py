import speech_recognition as sr
from gtts import gTTS
import os, time

robot_ears = sr.Recognizer()

def robot_say(answer_text):
    tts = gTTS(text=answer_text, lang='ru')
    if os.path.exists('bot_voice.mp3'):
        os.remove('bot_voice.mp3')
    tts.save('bot_voice.mp3')
    os.system('start bot_voice.mp3')
    time.sleep(len(answer_text) * 0.1 + 1)

with sr.Microphone() as mic:
    robot_ears.adjust_for_ambient_noise(mic, duration=1)
    while True:
        try:
            print("Слушаю...")
            audio = robot_ears.listen(mic, timeout=5, phrase_time_limit=5)
            text = robot_ears.recognize_google(audio, language='ru-RU').lower()
            print('Вы сказали:', text)
            if 'привет' in text:
                robot_say('Приветствую тебя человек!')
            elif 'как дела' in text:
                robot_say('Мои процессоры в норме Готов к работе')

        except sr.UnknownValueError:
            print('тишина или шум')
        except sr.WaitTimeoutError:
            print('Время ожидания истекло')
        except Exception as e:
            print('Ошибка:', e)
