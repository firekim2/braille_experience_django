from django.shortcuts import render
from .braille_translator_kor import kor_to_braille2
import random

def braille_viewer(request):
    text = [{'text':"오늘 밤에도 바람이 별에 스치운다.", 'author':"윤동주", 'title': "서시"}]
    text_choice = random.choice(text)
    result = kor_to_braille2.translate(text_choice.get('text'))
    return render(request, 'index.html', {'result': result, 'information': text_choice})


def audio_clip(request):
    return render(request, 'audio_clip.html')
