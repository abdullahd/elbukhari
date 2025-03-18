from django.shortcuts import render, get_object_or_404
from .models import Khutbah, Mohadarah, Sharhu, Motarjmah, Tilawah, Article, Announcement, Kitab
from django.db import models

# Create your views here.

def test_template(request):
    """Simple view to test template loading"""
    return render(request, 'test.html')

def khutbah_detail(request, khutbah_id):
    """View for displaying a single Khutbah entry"""
    khutbah = get_object_or_404(Khutbah, id=khutbah_id)
    
    # Increment hit counter
    khutbah.increment_hits()
    
    # Get related khutbahs (same sermon type or with common tags)
    related_khutbahs = Khutbah.objects.filter(
        models.Q(sermon_type=khutbah.sermon_type) | 
        models.Q(tags__in=khutbah.tags.all())
    ).exclude(id=khutbah.id).distinct()[:5]
    
    context = {
        'khutbah': khutbah,
        'page_title': khutbah.title,
        'related_khutbahs': related_khutbahs,
    }
    
    return render(request, 'pages/khutbah_detail.html', context)
