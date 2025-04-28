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

sound_path = 'input_good.wav' 
sound = AudioSegment.from_file(sound_path)
sound = sound.set_frame_rate(16000)

sound_path = sound_path.rsplit('.', 1)[0] + '_converted.wav'
sound.export(sound_path, format='wav')

text = recognize_speech(sound_path)
print(text)
