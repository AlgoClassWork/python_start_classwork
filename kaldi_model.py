from vosk import Model, KaldiRecognizer
import wave
import json
from pydub import AudioSegment

def convert_audio(wav_path):

    audio = AudioSegment.from_file(wav_path)
    audio = audio.set_channels(1).set_frame_rate(16000).set_sample_width(2)

    output_path = wav_path.rsplit('.', 1)[0] + '_converted.wav'
    audio.export(output_path, format='wav')
    return output_path

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
    texts.append(final_result.get('text',''))

    return ' '.join(texts)

converted_file = convert_audio('first_test.wav')
full_text = recognize_speech(converted_file)

print(full_text)
