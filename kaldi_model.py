from vosk import Model, KaldiRecognizer
import wave
import json
from pydub import AudioSegment


def recognize_speech(wav_path, model_path='vosk-model-small-ru-0.22'):

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    sound = wave.open(wav_path, 'rb')
    texts = []
    while True:
        data = sound.readframes(4000)
        if not data:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            texts.append(result.get('text',''))
    
    final_result = json.loads(recognizer.FinalResult())
    texts.append(result.get('text',''))

    return ' '.join(texts)

full_text = recognize_speech('first_test.wav')
print(full_text)
