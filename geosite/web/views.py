from django.shortcuts import render, get_object_or_404
from django.utils import timezone
#from .models import Report
from django.shortcuts import redirect

def index(request):
    #index = get_object_or_404(Index, pk=pk)
    return render(request, 'web/index.html', { })