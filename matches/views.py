from django.shortcuts import render, get_object_or_404
from matches.models import Match

def index(request):
    all_matches = Match.objects.all()
    context = {'all_matches': all_matches}
    return render(request, 'matches/index.html', context)

def detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    context = {'match': match}
    return render(request, 'matches/detail.html', context)
