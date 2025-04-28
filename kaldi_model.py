from vosk import Model, KaldiRecognizer
import wave 
import json
from pydub import AudioSegment

def recognize_speech(sound_name, model_path='vosk-model-small-ru-0.22'):
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    text = []
    sound = wave.open(sound_name, 'rb')
    while True:
        data = sound.readframes(4000)
        if not data:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text.append( result.get('text', '') )

    result = json.loads(recognizer.FinalResult())
    text.append( result.get('text', '') )

    return ' '.join(text)

text = recognize_speech('first_test.wav')
print(text)
