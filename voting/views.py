from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import timedelta
from .models import Feeling
import json

def index(request):
    return render(request, "voting/index.html")

@csrf_exempt
def handle_emoji_click(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        emoji_code = data.get('emoji')
        Feeling.objects.create(emoji=emoji_code)
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'}, status=400)

def emoji_percentage(request):
    feelings = Feeling.objects.all()
    
    emoji_counts = {}
    total_count = feelings.count()

    for feeling in feelings:
        emoji_counts[feeling.emoji] = emoji_counts.get(feeling.emoji, 0) + 1

    percentages = {emoji: (count / total_count) * 100 for emoji, count in emoji_counts.items()}

    return JsonResponse(percentages)