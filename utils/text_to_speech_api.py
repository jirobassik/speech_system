import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.name_voices = {'female': self.voices[1].id, 'male': self.voices[0].id}

    def set_engine_properties(self, rate, volume, voice):
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        self.engine.setProperty('voice', self.name_voices.get(voice))

    def run_tts(self, text):
        self.engine.save_to_file(text, 'media/audio.mp3')
        self.engine.runAndWait()
