from django.shortcuts import render
from django.http import JsonResponse
from .models import Conversation
import random

def index(request):
    return render(request, 'simplechat/index.html')

def get_conversation(request):
    level = request.GET.get('level', 'beginner')
    conversations = Conversation.objects.filter(level=level)
    if conversations:
        conversation = random.choice(conversations)
        data = {
            'dialogue': [
                {'english': d.english, 'chinese': d.chinese}
                for d in conversation.dialogues.all()
            ]
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'No conversation found'}, status=404)