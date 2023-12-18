from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import timedelta
from .models import Feeling, Country
import json

def index(request):
    return render(request, "voting/index.html")

@csrf_exempt
def handle_emoji_click(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        emoji_code = data.get('emoji')
        country_name = data.get('country', None)

        country = None
        if country_name:
            country, _ = Country.objects.get_or_create(name=country_name)

        Feeling.objects.create(emoji=emoji_code, country=country)
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'}, status=400)

def emoji_percentage(request):
    now = timezone.now()
    start_time = now - timedelta(days=1)
    feelings = Feeling.objects.filter(timestamp__gte=start_time)
    
    emoji_counts = {}
    total_count = feelings.count()

    for feeling in feelings:
        emoji_counts[feeling.emoji] = emoji_counts.get(feeling.emoji, 0) + 1

    percentages = {emoji: (count / total_count) * 100 for emoji, count in emoji_counts.items()}

    return JsonResponse(percentages)