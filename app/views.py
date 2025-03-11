from django.shortcuts import render

# Create your views here.

def test_template(request):
    """Simple view to test template loading"""
    return render(request, 'test.html')
