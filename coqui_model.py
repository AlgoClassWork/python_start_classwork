#pip install coqui-tts
from TTS.api import TTS

tts = TTS(model_name='tts_model/en/ljspeech/tacotron2-DDC',
          text='Hello world!')

tts.tts_to_file(text=text, file_path='test.wav')
