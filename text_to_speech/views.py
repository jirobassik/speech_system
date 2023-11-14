from time import sleep

from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.conf import settings
from text_to_speech.forms import TextToSpeechForm
from utils.text_to_speech_api import TextToSpeech

tts = TextToSpeech()


class TextToSpeechView(FormView):
    form_class = TextToSpeechForm
    template_name = 'text_to_speech/text_to_speech_view.html'
    success_url = reverse_lazy('audio-res')

    def form_valid(self, form):
        text = form.cleaned_data.get('text')
        rate = form.cleaned_data.get('rate')
        volume = form.cleaned_data.get('volume')
        dictor = form.cleaned_data.get('dictor')
        tts.set_engine_properties(rate, volume, dictor)
        tts.run_tts(text)
        sleep(5)
        return super().form_valid(form)


class AudioView(TemplateView):
    template_name = 'text_to_speech/work_result.html'
    extra_context = {'audio': settings.MEDIA_URL + 'audio.mp3'}
