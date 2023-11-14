from django.urls import path
from text_to_speech.views import TextToSpeechView, AudioView

urlpatterns = [
    path('', TextToSpeechView.as_view(), name='text-to-speech-view'),
    path('audio-result/', AudioView.as_view(), name='audio-res')
]